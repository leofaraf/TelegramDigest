import openai
from openai import OpenAI
import settings

openai.api_key = settings.OPENAI_API_KEY


def get_summary_text(text):
    return get_summary(text).choices[0].message.content


def get_summary(text):
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": settings.OPENAI_SYSTEM_ROLE},
            {"role": "user", "content": text}
        ]
    )
    return completion
