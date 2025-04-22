# Image transcribing

A FastAPI application that extracts text from images using OpenAI's Vision API and converts the extracted text to PDF files.

## Overview

This application provides a RESTful API that accepts images (either via URL or base64 encoded data) and uses OpenAI's Vision capabilities to extract text from these images in a structured format. The extracted text is then saved as a PDF file in the `created_files` directory.

## Features

- Process images from URLs
- Process base64 encoded images
- Extract text using OpenAI's Vision models
- Convert extracted text to PDF files
- Input validation using Pydantic
- Error handling with appropriate HTTP status codes

## Project Structure

```
marrow_test/
├── api/
│   └── image.py            # API endpoints for image processing
├── open_ai/
│   ├── base_encoded_image_processing.py   # Handles base64 encoded images
│   └── url_image_processing.py            # Handles image URLs
├── schemas/
│   └── image.py            # Pydantic models for request validation
├── created_files/          # Directory for storing generated PDFs
├── main.py                 # FastAPI application entry point
└── utils.py                # Utility functions (PDF generation)
```

## Prerequisites

- Python 3.11 or higher
- OpenAI API key

## Installation

This project uses Poetry for dependency management. To install:

```bash
cd marrow_test

# Install dependencies
poetry install
```

## Environment Variables

Create a `.env` file in the project root with:

```
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4.1-mini    # Optional: defaults to gpt-4.1-mini
```

## Running the Application

```bash
# Activate the poetry environment
poetry shell

# Run the application
python -m marrow_test.main
```

The API server will start on `http://0.0.0.0:8002`.

## API Usage

### Extract Text from Image

**Endpoint**: `POST /image/transcribe-image`

**Request Body**:

You must provide either `image_url` or `image_file_base_encoded`:

```json
{
  "image_url": "https://example.com/image.jpg"
}
```

OR

```json
{
  "image_file_base_encoded": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEA..."
}
```

**Response (Success)**:

```json
{
  "status": "ok",
  "text": "Extracted text from the image...",
  "file_name": "df124869-4ca7-4232-9d9f-97da959390a5.pdf"
}
```

**Response (Error)**:

```json
{
  "status": "error",
  "message": "Validation error",
  // "details": [
  //   {
  //     "type": "value_error",
  //     "loc": ["image_url"],
  //     "msg": "Invalid image URL",
  //     "input": "invalid-url"
  //   }
  // ]
}
```

## Error Handling

The API returns appropriate HTTP status codes:

- 200: Successful operation
- 400: Bad request (validation error)
- 500: Internal server error

## Dependencies

- FastAPI: Web framework
- Uvicorn: ASGI server
- Pydantic: Data validation
- OpenAI: API client for image processing
- PyMuPDF: PDF creation
