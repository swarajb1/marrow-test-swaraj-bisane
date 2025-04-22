import os

import openai
from openai import OpenAI

client = OpenAI()

# Analyze the content of an image

openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")


# @overload
# def generate_response_with_image_url(
#     question: str,
#     image_url: str,
#     raise_error: Literal[True] = True,
# ) -> str: ...


def generate_response_with_image_url(question: str, image_url: str, raise_error=False):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": question,
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url,
                                "detail": "auto",
                            },
                        },
                    ],
                },
            ],
        )

        return {"response": response.choices[0].message.content}

    except Exception as e:
        return {"error": f"OpenAI {MODEL} API error: " + str(e)}
