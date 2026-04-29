import requests
import os

GEMMA_API_KEY = os.getenv("GEMMA_API_KEY")

def parse_with_gemma(prompt):
    system_prompt = """
Extract trading info from user input.

Return ONLY JSON:
{
 "symbol": "BTC/USDT",
 "timeframes": ["1h"],
 "analysis": ["support","resistance"]
}
"""

    response = requests.post(
        "https://generativelanguage.googleapis.com/v1/models/gemma:generateContent?key=" + GEMMA_API_KEY,
        json={
            "contents": [{
                "parts": [{"text": system_prompt + "\nUser: " + prompt}]
            }]
        }
    )

    text = response.json()["candidates"][0]["content"]["parts"][0]["text"]

    import json
    return json.loads(text)
