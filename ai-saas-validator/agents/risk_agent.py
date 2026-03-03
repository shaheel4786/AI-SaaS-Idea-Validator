import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def risk_agent(idea: str) -> dict:
    """
    Performs risk assessment analysis.
    Returns structured JSON output.
    """

    prompt = f"""
    You are a Startup Risk Assessment Expert.

    Analyze the following startup idea:
    {idea}

    Provide:
    1. Technical Risks
    2. Market Adoption Risks
    3. Regulatory Risks
    4. Operational Risks
    5. Overall Risk Score (Low/Medium/High)
    6. Risk Explanation

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
        return {"error": "Invalid JSON returned from Risk Agent"}