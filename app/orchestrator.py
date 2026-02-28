from agents.resume_agent import analyze_resume
from agents.gap_agent import analyze_skill_gap
from agents.prioritizer_agent import prioritize_gap
from agents.strategy_agent import generate_learning_strategy
from agents.interview_agent import generate_interview_strategy


def run_career_pipeline(resume_text: str, target_role: str):

    resume_data = analyze_resume(resume_text)

    gap_analysis = analyze_skill_gap(resume_data, target_role)

    prioritized_plan = prioritize_gap(resume_data, gap_analysis, target_role)

    strategy = generate_learning_strategy(prioritized_plan, target_role)

    interview_strategy = generate_interview_strategy(resume_data, target_role)

    return {
        "resume_analysis": resume_data,
        "skill_gap": gap_analysis,
        "prioritized_focus": prioritized_plan,
        "strategy": strategy,
        "interview_preparation": interview_strategy
    }