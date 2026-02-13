import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_resume(resume_text, job_description):

    prompt = f"""

You are an ATS and resume expert.

TASK:
Compare the resume with the job description and respond in a consice, professional manner.

RULES:
- No Fluff
- No motivational talk
- Be precise
- Use bullet points
- Output must follow the exact format below

OUTPUT FORMAT:

Match Percentage: <number between 0-100>

Fit Verdict: <Stronger fit | Moderate fit | Weak fit>

Strengths:
- Bullet points

Missing or Weak Points:
- Bullet points

Resume Improvement Suggestions:
- bullet points with exact skills or wording to add

Errors Found:
- Grammar/spelling/clarity issues (If any)

Resume:
{resume_text}

Job Description:
{job_description}

"""
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content