import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from orchestrator import run_career_pipeline
from core.utils import extract_text_from_pdf

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="AI Career Strategy Engine",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# STYLING
# ==========================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
.stApp {
    background-color: #f6f8fc;
}
#MainMenu, footer, header { visibility: hidden; }

/* HERO */
.hero {
    background: linear-gradient(135deg, #1e3a8a, #4f46e5);
    padding: 3rem 3.2rem;
    border-radius: 0 0 32px 32px;
    margin-bottom: 2.5rem;
    box-shadow: 0 10px 30px rgba(30,58,138,0.15);
}
.hero h1 {
    color: white;
    font-size: 2.4rem;
    font-weight: 800;
    margin-bottom: 0.6rem;
}
.hero p {
    color: rgba(255,255,255,0.78);
    font-size: 0.95rem;
    max-width: 600px;
}

/* SECTION TITLE */
.section-title {
    font-size: 1.25rem;
    font-weight: 700;
    margin: 2.4rem 0 1.2rem 0;
    color: #0f172a;
    letter-spacing: -0.3px;
}

/* CARD */
.card {
    background: white;
    padding: 1.6rem 1.8rem;
    border-radius: 18px;
    border: 1px solid #e2e8f0;
    margin-bottom: 1.4rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    transition: all 0.2s ease;
}
.card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.06);
}

/* SKILL TAG */
.skill-tag {
    background: #eef2ff;
    color: #3730a3;
    padding: 6px 14px;
    border-radius: 100px;
    font-size: 0.78rem;
    font-weight: 600;
    display: inline-block;
    margin: 5px 5px 0 0;
}

/* GAP BOX */
.gap-box {
    background: white;
    border-radius: 18px;
    padding: 1.6rem;
    border: 1px solid #e2e8f0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
}
.gap-title {
    font-weight: 700;
    font-size: 0.95rem;
    margin-bottom: 1rem;
}
.gap-item {
    padding: 10px 12px;
    border-radius: 10px;
    margin-bottom: 8px;
    font-size: 0.85rem;
}
.gap-missing {
    background: #fef2f2;
    border-left: 4px solid #dc2626;
}
.gap-priority {
    background: #eff6ff;
    border-left: 4px solid #2563eb;
}

/* SCORE CARD */
.score-card {
    background: linear-gradient(135deg, #eef2ff, #f8fafc);
    border-radius: 22px;
    padding: 2rem 2.2rem;
    border: 1px solid #e0e7ff;
}
.score-big {
    font-size: 3.5rem;
    font-weight: 800;
    color: #1e3a8a;
}
.score-label {
    font-size: 0.9rem;
    color: #64748b;
}

/* INTERVIEW GRID */
.interview-tag {
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    padding: 7px 10px;
    border-radius: 10px;
    font-size: 0.75rem;
    font-weight: 500;
    text-align: center;
}

/* DOWNLOAD */
.stDownloadButton > button {
    background: linear-gradient(135deg, #1e3a8a, #4f46e5) !important;
    color: white !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 0.6rem 1.8rem !important;
    border: none !important;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# HERO
# ==========================================
st.markdown("""
<div class="hero">
    <h1>AI Career Strategy Engine</h1>
    <p>Structured skill gap analysis, 4-week roadmap, and focused interview preparation — powered by AI.</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# INPUT
# ==========================================
col1, col2 = st.columns([1, 1])

with col1:
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

with col2:
    target_role = st.text_input("Target Role", value="Machine Learning Intern")

analyze = st.button("Generate Career Strategy", use_container_width=True)

# ==========================================
# PIPELINE
# ==========================================
if analyze:

    if not uploaded_file:
        st.error("Please upload a resume first.")
    else:
        with st.spinner("Analyzing profile..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            result = run_career_pipeline(resume_text, target_role)

        # PROFILE SUMMARY
        st.markdown('<div class="section-title">Profile Summary</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card">{result.get("resume_analysis", {}).get("summary","")}</div>', unsafe_allow_html=True)

        # CORE SKILLS
        st.markdown('<div class="section-title">Core Skills</div>', unsafe_allow_html=True)
        skills = result.get("resume_analysis", {}).get("skills", [])
        tags = "".join([f'<span class="skill-tag">{s}</span>' for s in skills])
        st.markdown(f'<div class="card">{tags}</div>', unsafe_allow_html=True)

        # SKILL GAP
        st.markdown('<div class="section-title">Skill Gap Analysis</div>', unsafe_allow_html=True)

        gap = result.get("skill_gap", {})
        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.markdown('<div class="gap-box">', unsafe_allow_html=True)
            st.markdown('<div class="gap-title" style="color:#dc2626;">Missing Skills</div>', unsafe_allow_html=True)
            for s in gap.get("missing_skills", []):
                st.markdown(f'<div class="gap-item gap-missing">{s}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="gap-box">', unsafe_allow_html=True)
            st.markdown('<div class="gap-title" style="color:#2563eb;">Priority Skills</div>', unsafe_allow_html=True)
            for s in gap.get("priority_skills_to_learn", []):
                st.markdown(f'<div class="gap-item gap-priority">{s}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # ROLE READINESS
        missing = len(gap.get("missing_skills", []))
        partial = len(gap.get("partially_matching_skills", []))
        total = missing + partial
        score = int((partial / total) * 100) if total > 0 else 80

        st.markdown('<div class="section-title">Role Readiness</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="score-card">
            <div class="score-big">{score}%</div>
            <div class="score-label">Match Score</div>
        </div>
        """, unsafe_allow_html=True)

        # ROADMAP
        st.markdown('<div class="section-title">4-Week Roadmap</div>', unsafe_allow_html=True)

        strategy = result.get("strategy", {})
        st.markdown(f'<div class="card"><b>Project:</b> {strategy.get("project_title","")}<br><br>{strategy.get("project_description","")}</div>', unsafe_allow_html=True)

        for week in strategy.get("weeks", []):
            with st.expander(f"Week {week.get('week')} — {week.get('focus')}"):
                st.markdown(f"**Goal:** {week.get('clear_goal')}")
                st.markdown("**Action Steps:**")
                for task in week.get("actionable_tasks", []):
                    st.markdown(f"- {task}")
                st.markdown(f"**Deliverable:** {week.get('measurable_deliverable')}")
                st.markdown(f"**Portfolio:** {week.get('portfolio_output')}")

        # INTERVIEW
        st.markdown('<div class="section-title">Interview Preparation</div>', unsafe_allow_html=True)
        interview = result.get("interview_preparation", {})
        tech_topics = interview.get("technical_topics_to_prepare", [])

        if tech_topics:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            cols = st.columns(4)
            for i, topic in enumerate(tech_topics):
                with cols[i % 4]:
                    st.markdown(f'<div class="interview-tag">{topic}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # DOWNLOAD
        json_report = json.dumps(result, indent=2)
        st.download_button(
            "Download JSON Report",
            data=json_report,
            file_name="career_strategy_report.json",
            mime="application/json"
        )