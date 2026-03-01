# AI Career Strategy Engine

A deployed AI-based web application that analyzes a resume against a target role and generates structured career guidance including skill gap analysis, a 4-week roadmap, and interview preparation suggestions.

Live App: https://your-streamlit-link.streamlit.app  
Repository: https://github.com/farajt/ai-career-strategy-engine

---

## Project Overview

This project is built to simulate how a candidate can evaluate their readiness for a specific role using AI.

The user uploads a resume (PDF) and enters a target role. The system then:

- Extracts resume content
- Identifies strengths and skills
- Detects missing and partially matching skills
- Generates a focused 4-week improvement roadmap
- Suggests interview preparation topics
- Calculates a role readiness score

The application is fully deployed and publicly accessible.

---

## What This Project Demonstrates

- Practical use of LLMs in a structured pipeline
- Multi-agent modular architecture
- Prompt engineering with structured JSON outputs
- Production deployment using Streamlit Cloud
- Secure API key management
- Clean UI rendering of AI-generated outputs

This is not just a notebook experiment — it is a deployed AI system.

---

## Architecture

The system follows a modular agent-based pipeline:

User Resume (PDF)  
→ Text Extraction (pypdf)  
→ Resume Analysis Agent  
→ Skill Gap Agent  
→ Prioritization Agent  
→ Strategy Agent (4-week roadmap)  
→ Interview Preparation Agent  
→ Structured JSON Output  
→ Streamlit UI Rendering  

Each stage is isolated and handled by a dedicated module for clarity and scalability.

---

## Tech Stack

Backend:
- Python
- LangChain
- Groq API (LLM inference)
- Pydantic (structured output validation)

Frontend:
- Streamlit

Deployment:
- Streamlit Cloud
- GitHub
- Environment-based secret management

---

## How It Works

1. Resume Parsing  
   The uploaded PDF is parsed using `pypdf` to extract raw text.

2. Resume Analysis  
   The LLM analyzes the resume and extracts summary and skills.

3. Skill Gap Analysis  
   The system compares extracted skills against the target role and identifies:
   - Missing skills
   - Partially matching skills
   - Priority skills to focus on

4. Strategic Focus  
   The engine identifies the primary gap and defines a 4-week improvement direction.

5. Roadmap Generation  
   A structured weekly roadmap is generated with:
   - Clear goal
   - Action steps
   - Measurable deliverable
   - Portfolio output

6. Interview Preparation  
   The system suggests:
   - Technical topics
   - System design areas
   - Behavioral questions

7. UI Rendering  
   The structured output is displayed in a clean and organized dashboard.

---

## Possible Improvements

- User authentication
- Usage rate limiting
- Saving historical reports
- Role-specific templates
- Analytics dashboard

---

## Author

Faraj Tamboli  
M.Tech CSE (AI)  
Interested in LLM systems, applied AI, and production ML engineering.