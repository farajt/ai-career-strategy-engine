import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def get_llm_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in .env file")

    client = Groq(api_key=api_key)
    return client


import json
from typing import Dict


def generate_structured_response(prompt: str) -> Dict:
    client = get_llm_client()

    system_prompt = """
You are an AI that ALWAYS responds in valid JSON format.
Do not write explanations.
Return only valid JSON.
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    response_text = completion.choices[0].message.content

    try:
        return json.loads(response_text)
    except:
        raise ValueError(f"Invalid JSON returned:\n{response_text}")