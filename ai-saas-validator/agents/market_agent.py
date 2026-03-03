import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def market_agent(idea: str) -> dict:
    """
    Performs market research analysis for a startup idea.
    Returns structured JSON output.
    """

    prompt = f"""
    You are a Market Research Analyst.

    Analyze the following startup idea:
    {idea}

    Provide:
    1. Industry Name
    2. Industry Trends (bullet points)
    3. TAM (Total Addressable Market)
    4. SAM (Serviceable Addressable Market)
    5. SOM (Serviceable Obtainable Market)
    6. Target Audience
    7. Estimated Growth Rate

    Return response strictly in JSON format.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    try:
        return json.loads(response.choices[0].message.content)
    except:
        return {"error": "Invalid JSON returned from Market Agent"}