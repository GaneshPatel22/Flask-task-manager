import os
from pathlib import Path

import requests
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise Exception("OPENROUTER_API_KEY not found in .env")


def generate_profile(name, context, sources):

    prompt = f"""
Create a professional profile.

Person: {name}

Information:
{context}

Sources:
{sources}

Return markdown in this format:

# {name}

## Introduction

## Career

## Achievements

## Interesting Facts

## References
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5000",
        "X-Title": "AI Profile Builder"
    }

    body = {
        "model": "openrouter/free",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=body,
        timeout=60
    )

    if response.status_code != 200:
        raise Exception(response.text)

    data = response.json()

    import json

    import json
    print(json.dumps(data, indent=2))



    return data["choices"][0]["message"]["content"]