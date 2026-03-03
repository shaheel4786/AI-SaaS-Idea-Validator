import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def competitor_agent(idea: str) -> dict:
    """
    Identifies competitors and analyzes features & pricing.
    Returns structured JSON output.
    """

    prompt = f"""
    You are a Competitive Intelligence Analyst.

    Analyze the following startup idea:
    {idea}

    Provide:
    1. Direct Competitors (name + short description)
    2. Indirect Competitors
    3. Key Features Comparison
    4. Pricing Models Used
    5. Competitive Intensity (Low/Medium/High)

    Return strictly in JSON format.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    try:
        return json.loads(response.choices[0].message.content)
    except:
        return {"error": "Invalid JSON returned from Competitor Agent"}