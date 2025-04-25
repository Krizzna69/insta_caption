import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from environment
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    print("Error: GEMINI_API_KEY not found in environment variables")
    exit(1)

# Configure the API
genai.configure(api_key=api_key)

# Test with a simple text prompt
model = genai.GenerativeModel('gemini-2.0-flash')
try:
    response = model.generate_content("Hello, world!")
    print("API connection successful!")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error connecting to Gemini API: {e}")