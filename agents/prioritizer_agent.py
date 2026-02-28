from core.llm_config import generate_structured_response


def prioritize_gap(resume_data: dict, gap_analysis: dict, target_role: str):
    prompt = f"""
You are a Senior Career Strategy Analyst.

Resume Data:
{resume_data}

Skill Gap Analysis:
{gap_analysis}

Target Role:
{target_role}

Task:

1. Identify the candidate's strongest 3 competencies.
2. From the missing skills list, identify the SINGLE most critical gap
   blocking internship readiness.
3. Explain why that gap is more important than others.
4. Define one focused improvement pillar for the next 4 weeks.

Return JSON in this format:

{{
  "top_strengths": [],
  "primary_gap": "",
  "reason_for_priority": "",
  "focus_pillar": ""
}}
"""

    return generate_structured_response(prompt)