import os
from typing import Literal, NoReturn, overload

import openai
from openai import OpenAI

client = OpenAI()

# Analyze the content of an image

openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")


@overload
def generate_response_with_image_url(
    question: str,
    image_url: str,
    raise_error: Literal[True] = True,
) -> str:
    ...


def generate_response_with_image_url(question: str, image_url: str, raise_error=False) -> str | None | NoReturn:
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

        return response.choices[0].message.content

    except Exception as e:
        if raise_error:
            raise RuntimeError(f"OpenAI {MODEL} API error: " + str(e))
        else:
            print(f"OpenAI {MODEL} API error: " + str(e))

    return None
