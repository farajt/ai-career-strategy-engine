from core.llm_config import generate_structured_response


def analyze_resume(resume_text: str):
    prompt = f"""
You are a Resume Analysis Agent.

Extract structured information from the resume below.

Return JSON in this format:
{{
  "summary": "",
  "skills": [],
  "experience_years": "",
  "projects": [],
  "education": []
}}

Resume:
{resume_text}
"""

    return generate_structured_response(prompt)