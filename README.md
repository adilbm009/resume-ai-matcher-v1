# AI Resume–Job Description Matcher (GenAI Project)

## Overview
This project is a GenAI-powered application that analyzes how well a resume matches a given job description.  
It simulates an ATS-style evaluation by calculating a match score, identifying strengths and gaps, and suggesting targeted resume improvements.

The goal of this project was to **learn practical GenAI development** by building an end-to-end application, focusing on prompt engineering, document processing, and deployment-ready architecture.

---

## Features
- Upload resumes in **PDF** or **DOCX** format
- Paste any job description as input
- Extracts and cleans resume text automatically
- Uses a Large Language Model (LLM) to:
  - Calculate resume–job match percentage (0–100)
  - Provide a fit verdict (Strong / Moderate / Weak)
  - Highlight matching strengths
  - Identify missing or weak skills
  - Suggest specific resume improvements
  - Detect grammar, spelling, and clarity issues
- Concise, structured, and ATS-style output (no unnecessary text)

---

## Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python
- **LLM:** Groq API (LLaMA 3)
- **Libraries:**
  - pypdf (PDF text extraction)
  - python-docx (DOCX text extraction)
- **Deployment Ready:** Streamlit Cloud compatible
- **Version Control:** Git & GitHub

---

## Project Architecture
resume_ai/
│
├── app.py                # Streamlit application
├── requirements.txt      # Project dependencies
├── utils/
│   ├── file_loader.py    # File type handling
│   ├── text_extractor.py # PDF/DOCX text extraction
│   └── llm_client.py     # LLM API interaction


The project is structured to clearly separate:
- UI logic
- File handling
- Text extraction
- LLM interaction

This makes the codebase easy to extend (e.g., adding RAG or agents in future versions).

---

## How It Works
1. User uploads a resume (PDF/DOCX)
2. Resume text is extracted and cleaned
3. User provides a job description
4. A structured prompt is sent to the LLM
5. The LLM returns a deterministic, formatted analysis
6. Results are displayed in the UI

---

## Key Learning Outcomes
- Practical prompt engineering for structured LLM output
- Handling unstructured documents for GenAI applications
- Designing deterministic and resume-safe AI responses
- Secure API key management using environment variables
- Deploying a production-ready GenAI application

