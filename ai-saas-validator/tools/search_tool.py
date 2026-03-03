import os
import requests

SERPER_API_KEY = os.getenv("SERPER_API_KEY")

def google_search(query: str, num_results: int = 5):
    """
    Performs Google search using Serper API.
    Returns top search results.
    """

    url = "https://google.serper.dev/search"

    payload = {
        "q": query,
        "num": num_results
    }

    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        results = []

        for item in data.get("organic", []):
            results.append({
                "title": item.get("title"),
                "link": item.get("link"),
                "snippet": item.get("snippet")
            })

        return results
    else:
        return {"error": "Search API failed"}