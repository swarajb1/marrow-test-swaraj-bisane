# 🖼️ Image Transcriber API

This project is a REST API for extracting text from images using OpenAI's Vision API and exporting the text to a PDF.

## 🔧 Features

- Accepts image input via:
  - Public URL
  - Base64-encoded string
- Uses OpenAI GPT-4 Vision for transcription
- Saves transcribed text to a PDF on the server
- Robust error handling

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API Key

### Installation

```bash
git clone https://github.com/yourusername/image-transcriber.git
cd image-transcriber
pip install -r requirements.txt
