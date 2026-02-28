from core.llm_config import generate_structured_response


def generate_learning_strategy(prioritized_plan: dict, target_role: str):

    prompt = f"""
You are a Senior Hiring Manager at a product-based tech company.

Prioritized Focus Plan:
{prioritized_plan}

Target Role:
{target_role}

Design a realistic 4-week internship-preparation roadmap.

Rules:

- Build ONE focused project aligned with the primary gap.
- Avoid generic tutorials.
- Avoid "read articles" or "watch courses".
- Avoid research-paper suggestions.
- Keep scope realistic for 4 weeks.
- Each week must build toward a deployable, GitHub-ready project.
- Focus on practical implementation, testing, and documentation.

Each week must include:

- focus
- clear_goal
- actionable_tasks (plain strings only)
- measurable_deliverable
- portfolio_output

Return JSON in this format:

{{
  "project_title": "",
  "project_description": "",
  "weeks": [
    {{
      "week": 1,
      "focus": "",
      "clear_goal": "",
      "actionable_tasks": [],
      "measurable_deliverable": "",
      "portfolio_output": ""
    }}
  ],
  "final_outcome": ""
}}
"""

    return generate_structured_response(prompt)