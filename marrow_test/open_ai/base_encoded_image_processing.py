import os

import openai
from openai import OpenAI

openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

MODEL = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")


# @overload
# def generate_response_with_image_base_encoded(
#     question: str,
#     image_file_base_encoded: str,
#     raise_error: Literal[True] = True,
# ) -> str: ...


def generate_response_with_image_base_encoded(
    question: str,
    image_file_base_encoded: str,
):
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
                                "url": image_file_base_encoded,
                            },
                        },
                    ],
                },
            ],
        )

        return {"response": response.choices[0].message.content}

    except Exception as e:
        return {
            "error": f"OpenAI {MODEL} API error: " + str(e),
            "code": e.status_code if hasattr(e, "status_code") else 500,
        }
