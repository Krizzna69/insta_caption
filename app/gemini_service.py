import google.generativeai as genai
import base64
from PIL import Image
import io

class GeminiService:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        # Initialize Gemini 2.5 model
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def _prepare_image(self, image_file):
        """Process uploaded image for Gemini API"""
        image = Image.open(image_file)

        # Convert RGBA to RGB (remove transparency)
        if image.mode == 'RGBA':
            # Create a white background image
            background = Image.new('RGB', image.size, (255, 255, 255))
            # Paste the image on the background using alpha as mask
            background.paste(image, mask=image.split()[3])
            image = background
        elif image.mode != 'RGB':
            # Convert any other mode to RGB
            image = image.convert('RGB')

        # Resize if necessary (optional)
        max_size = 1024
        if max(image.size) > max_size:
            ratio = max_size / max(image.size)
            new_size = (int(image.size[0] * ratio), int(image.size[1] * ratio))
            image = image.resize(new_size, Image.LANCZOS)

        return image

    def generate_caption(self, image_file, style="engaging"):
        """Generate Instagram caption based on image and style"""
        try:
            image = self._prepare_image(image_file)

            # Create prompt based on selected style
            style_prompts = {
                "funny": "Create a humorous Instagram caption with a touch of wit",
                "aesthetic": "Create a visually descriptive, aesthetic Instagram caption",
                "poetic": "Create a poetic, emotional Instagram caption",
                "minimalist": "Create a short, impactful Instagram caption with few words",
                "engaging": "Create an engaging Instagram caption that will drive comments"
            }

            style_prompt = style_prompts.get(style.lower(), style_prompts["engaging"])

            prompt = f"""
            You are a professional social media content creator specializing in Instagram captions.

            Analyze this image and:
            1. {style_prompt} that captures the essence of this image (3-4 sentences maximum).
            2. Generate 15-20 relevant hashtags that will maximize reach.

            Format your response as:
            CAPTION: [Your caption here]

            HASHTAGS: [Your hashtags here, each starting with #]
            """

            print("Sending request to Gemini API...")
            response = self.model.generate_content([prompt, image])
            print("Received response from Gemini API")

            # Parse response
            text_response = response.text

            # Fallback for unusual formatting
            if "CAPTION:" not in text_response:
                parts = text_response.split("\n\n", 1)
                caption_part = parts[0].strip()
                hashtags_part = parts[1].strip() if len(parts) > 1 else ""
            else:
                caption_part = text_response.split("HASHTAGS:")[0].replace("CAPTION:", "").strip()
                hashtags_part = text_response.split("HASHTAGS:")[1].strip() if "HASHTAGS:" in text_response else ""

            return {
                "caption": caption_part,
                "hashtags": hashtags_part
            }
        except Exception as e:
            import traceback
            print(f"Error in generate_caption: {str(e)}")
            print(traceback.format_exc())
            raise