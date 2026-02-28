from core.llm_config import generate_structured_response


def generate_interview_strategy(resume_data: dict, target_role: str):
    prompt = f"""
You are an Interview Preparation Agent.

Candidate Resume:
{resume_data}

Target Role:
{target_role}

Return JSON in this format:
{{
  "technical_topics_to_prepare": [],
  "system_design_focus": [],
  "behavioral_questions_to_expect": [],
  "portfolio_improvements": [],
  "mock_interview_suggestions": []
}}
"""

    return generate_structured_response(prompt)