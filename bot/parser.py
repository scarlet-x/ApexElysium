import os
import json
import google.genai as genai

GEMMA_API_KEY = os.getenv("GEMMA_API_KEY")

def parse_with_gemma(prompt):
    client = genai.Client(api_key=GEMMA_API_KEY)
    
    system_prompt = """
Extract trading info from user input.

Return ONLY JSON:
{
 "symbol": "BTC/USDT",
 "timeframes": ["1h"],
 "analysis": ["support","resistance"]
}
"""

    response = client.models.generate_content(
        model="gemma-4",
        contents=system_prompt + "\nUser: " + prompt
    )

    text = response.text
    return json.loads(text)