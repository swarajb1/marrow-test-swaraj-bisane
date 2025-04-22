import os
from typing import Literal, NoReturn, overload

import openai
from openai import OpenAI

openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

MODEL = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")


@overload
def generate_response_with_image_base_encoded(
    question: str,
    image_file_base_encoded: str,
    raise_error: Literal[True] = True,
) -> str:
    ...


def generate_response_with_image_base_encoded(
    question: str,
    image_file_base_encoded: str,
    raise_error=False,
) -> str | None | NoReturn:
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

        return response.choices[0].message.content

    except Exception as e:
        if raise_error:
            raise RuntimeError(f"OpenAI {MODEL} API error: " + str(e))
        else:
            print(f"OpenAI {MODEL} API error: " + str(e))

    return None
