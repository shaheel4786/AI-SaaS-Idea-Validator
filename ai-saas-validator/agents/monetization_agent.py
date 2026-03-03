import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def monetization_agent(idea: str) -> dict:
    """
    Suggests monetization strategies and pricing.
    Returns structured JSON output.
    """

    prompt = f"""
    You are a SaaS Monetization Strategist.

    Analyze the following startup idea:
    {idea}

    Provide:
    1. Recommended Revenue Model
    2. Suggested Pricing Tiers (Basic/Pro/Enterprise)
    3. Upsell Strategies
    4. Revenue Assumptions (monthly projection example)
    5. Break-even Estimate

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
        return {"error": "Invalid JSON returned from Monetization Agent"}