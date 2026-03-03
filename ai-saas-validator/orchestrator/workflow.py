from agents.market_agent import market_agent
from agents.competitor_agent import competitor_agent
from agents.monetization_agent import monetization_agent
from agents.risk_agent import risk_agent

from tools.search_tool import google_search
from tools.vector_store import store_document

def run_full_workflow(idea: str):
    """
    Main orchestrator for multi-agent execution.
    """

    # Step 1: External Research
    search_results = google_search(idea)

    # Store search results in vector DB
    store_document("search_data", str(search_results))

    # Step 2: Agent Execution
    market = market_agent(idea)
    competitor = competitor_agent(idea)
    monetization = monetization_agent(idea)
    risk = risk_agent(idea)

    # Step 3: Aggregate Results
    final_report = {
        "search_data": search_results,
        "market_analysis": market,
        "competitor_analysis": competitor,
        "monetization_strategy": monetization,
        "risk_assessment": risk
    }

    return final_report