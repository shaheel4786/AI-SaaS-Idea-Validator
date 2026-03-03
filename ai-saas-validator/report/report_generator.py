def generate_executive_summary(results: dict) -> str:
    """
    Generates executive summary based on analysis.
    """

    market = results.get("market_analysis", {})
    competitor = results.get("competitor_analysis", {})
    risk = results.get("risk_assessment", {})

    risk_score = risk.get("Overall Risk Score", "Medium")

    summary = f"""
The startup idea operates in the **{market.get('Industry Name', 'identified industry')}** domain.

Market opportunity appears promising with TAM estimated at 
**{market.get('TAM', 'N/A')}**.

Competitive intensity is assessed as 
**{competitor.get('Competitive Intensity', 'Medium')}**.

Overall risk level is classified as **{risk_score}**.
"""

    return summary


def generate_go_no_go_decision(results: dict) -> str:
    """
    Basic decision logic based on risk and competition.
    """

    risk = results.get("risk_assessment", {})
    competitor = results.get("competitor_analysis", {})

    risk_score = risk.get("Overall Risk Score", "Medium")
    competition = competitor.get("Competitive Intensity", "Medium")

    if risk_score == "Low" and competition != "High":
        return "✅ GO – The idea shows promising potential with manageable risk."
    elif risk_score == "High":
        return "❌ NO-GO – Risk level is high. Further validation required before proceeding."
    else:
        return "⚠ CONDITIONAL GO – Consider MVP testing and further validation."


def format_section(title: str, content: dict) -> str:
    """
    Formats dictionary content into markdown section.
    """

    section_text = f"\n## {title}\n"

    if isinstance(content, dict):
        for key, value in content.items():
            section_text += f"\n**{key}:** {value}\n"
    else:
        section_text += f"\n{content}\n"

    return section_text


def generate_final_report(results: dict) -> str:
    """
    Generates full structured startup validation report.
    """

    executive_summary = generate_executive_summary(results)
    decision = generate_go_no_go_decision(results)

    report = f"""
# 🚀 AI SaaS Startup Idea Validation Report

---

## 📌 Executive Summary
{executive_summary}

---

{format_section("📈 Market Analysis", results.get("market_analysis", {}))}

---

{format_section("🏢 Competitor Landscape", results.get("competitor_analysis", {}))}

---

{format_section("💰 Monetization Strategy", results.get("monetization_strategy", {}))}

---

{format_section("⚠ Risk Assessment", results.get("risk_assessment", {}))}

---

## 🎯 Final Recommendation

{decision}

---

### 📎 Note:
This report is AI-generated and should be complemented with real-world validation and customer interviews.
"""

    return report