from flask import Blueprint, render_template, request, jsonify
from app.gemini_service import GeminiService
import os
from werkzeug.utils import secure_filename
from config import Config

main = Blueprint('main', __name__)
gemini_service = GeminiService(Config.GEMINI_API_KEY)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/generate', methods=['POST'])
def generate():
    # Debug output
    print("Request received at /generate")

    if 'image' not in request.files:
        print("No image file in request")
        return jsonify({'error': 'No image file uploaded'}), 400

    file = request.files['image']

    if file.filename == '':
        print("Empty filename")
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        style = request.form.get('style', 'engaging')
        print(f"Processing image: {file.filename} with style: {style}")

        try:
            result = gemini_service.generate_caption(file, style)
            return jsonify(result)
        except Exception as e:
            # Print the full error for debugging
            import traceback
            print(f"Error processing request: {str(e)}")
            print(traceback.format_exc())
            return jsonify({'error': str(e)}), 500

    return jsonify({'error': 'File type not allowed'}), 400