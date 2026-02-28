from core.llm_config import generate_structured_response


def analyze_skill_gap(resume_data: dict, target_role: str):
    prompt = f"""
You are a Skill Gap Analysis Agent.

Candidate Resume Data:
{resume_data}

Target Role:
{target_role}

Return JSON in this format:
{{
  "missing_skills": [],
  "partially_matching_skills": [],
  "priority_skills_to_learn": [],
  "recommended_projects": []
}}
"""

    return generate_structured_response(prompt)