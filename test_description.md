# Title: Image transcribing

Description
You are tasked with building a REST API that accepts an image as input (either via a URL or Base64 encoded string), utilizes the OpenAI Vision API to extract text from the image, and returns the transcribed text. The transcribed text should also be saved to a PDF file.

Technical Requirements:

- API Framework:
  - Implement the API using either FastAPI (Python).
- Input Methods:
  - The API must accept images through two methods:
  - URL: A publicly accessible URL pointing to the image.
  - Base64 encoded string: The image data encoded in Base64 format.
- OpenAI Vision API Integration:
  - Utilize the OpenAI Vision API
  - Ensure proper authentication and authorization with the OpenAI API.
  - API reference: <https://platform.openai.com/docs/guides/images?api-mode=chat>

PDF Output:
Save the transcribed text to a .pdf file.
The PDF file should be generated and saved on the server.
The file name should be generated dynamically.
Error Handling:
Implement robust error handling for various scenarios, including:
Invalid input (e.g., invalid URL, invalid Base64).
Network issues (e.g., OpenAI API connection errors).
OpenAI API errors (e.g., invalid API key, rate limits).
File system errors.
Return appropriate HTTP error codes and informative error messages in the API response.
Code Structure:
Organize the code into logical modules and functions.
Follow Python coding conventions and best practices.
Use comments to make the code easy to understand.
README File:
Create a comprehensive README.md file that explains the project
