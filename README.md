

# AI Caption & Hashtag Generator for Instagram

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Flask](https://img.shields.io/badge/Flask-2.3.0-red)
![License](https://img.shields.io/badge/license-MIT-yellow)

> A next-generation web application that leverages Google's Gemini 2.5 Multimodal API to generate engaging captions and relevant hashtags directly from your images.

## 🚀 Overview

The **AI Caption & Hashtag Generator** is designed for content creators, marketers, and everyday Instagram users. This tool automates the creative process of writing Instagram captions with zero manual effort by analyzing your images and generating context-aware, engaging text and hashtags.

Simply upload an image, select a caption style, and let the AI do the work for you!

<p align="center">
  <img src="https://via.placeholder.com/600x350/4285F4/FFFFFF?text=Instagram+Caption+Generator" alt="Instagram Caption Generator UI" width="600"/>
</p>

## ✨ Features

- **One-Click Caption Generation**: Upload any image → get smart, styled captions instantly
- **Multiple Caption Styles**: Choose from funny, aesthetic, poetic, minimalist, or engaging tones
- **Trending Hashtags**: Get context-aware hashtags that match your image content
- **Clean, Responsive UI**: User-friendly interface accessible from any device
- **Efficient Workflow**: Copy captions and hashtags to clipboard with a single click

## 🔧 Technology Stack

- **Frontend**: HTML, CSS, JavaScript with Bootstrap 5
- **Backend**: Python + Flask
- **AI Engine**: Google Gemini 2.5 Pro Multimodal API
- **Image Processing**: Pillow (PIL Fork)

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini API key (obtain from [Google AI Studio](https://ai.google.dev/))

## 🛠️ Installation

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/instagram-caption-generator.git
cd instagram-caption-generator
```

2. **Set up a virtual environment**:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Create a .env file with your API key**:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

5. **Create the necessary folders for static files**:

```bash
mkdir -p static/css static/js
```

6. **Run the application**:

```bash
python run.py
```

7. **Access the application**:
   - Open your browser and go to http://127.0.0.1:5000/

## 📝 Usage

1. **Open the web application in your browser**
2. **Upload an image** by clicking on the file input or dragging and dropping
3. **Select a caption style** from the dropdown menu:
   - Engaging (default)
   - Funny
   - Aesthetic
   - Poetic
   - Minimalist
4. **Click "Generate Caption"** and wait for the AI to work its magic
5. **Copy the caption and hashtags** using the provided buttons
6. **Paste directly into Instagram** or your scheduling tool

## ⚠️ Troubleshooting

### Images with Transparency

The application automatically handles images with transparency (RGBA mode) by converting them to RGB with a white background before processing.

### API Key Issues

If you encounter authentication errors:
1. Verify your API key in the `.env` file
2. Ensure the API key has access to Gemini 2.5 Pro model
3. Run the `test_gemini.py` script to verify API connectivity:

```bash
python test_gemini.py
```

### Missing Static Files

If you see 404 errors for CSS or JavaScript files:
1. Ensure you've created the proper directory structure for static files
2. Make sure the static files are in the correct location

## 📚 Project Structure

```
instagram-caption-generator/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── gemini_service.py
│   └── templates/
│       └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── .env
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google for providing the powerful Gemini 2.5 API
- Flask community for excellent documentation and examples
- Bootstrap team for responsive UI components

## 📧 Contact

Questions or feedback? Reach out or open an issue on GitHub!

---

*Made with ❤️ for Instagram content creators everywhere*
