import streamlit as st
from utils.file_loader import get_file_extension
from utils.text_extractor import(
    extract_text_from_docx,
    extract_text_from_pdf
)
from utils.llm_client import analyze_resume


st.set_page_config(page_title="Resume Matcher", layout="centered")

st.title("Resume Vs Job Description AI")

uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF or DOCX)",
    type = ["pdf", "docx"]
)

job_description = st.text_area(
    "paste job description",
    height=200
)



if uploaded_file:
    file_ext = get_file_extension(uploaded_file)

    if file_ext == ".pdf":
        resume_text = extract_text_from_pdf(uploaded_file)
    elif file_ext == ".docx":
        resume_text = extract_text_from_docx(uploaded_file)
    else:
        st.error("Unsupported file format")
        st.stop()
    
    if not resume_text.strip():
        st.error("Could not extract text from resume")
        st.stop()
    
    st.success("Resume text extracted successfully")
    
    if st.button("Analyze Resume"):
        with st.spinner("Analyzing resume..."):
            result = analyze_resume(resume_text, job_description)


        st.success("Analysis Complete")
        st.markdown(result)
    
    

    