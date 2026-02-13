from pypdf import PdfReader
from docx import Document

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = []
    for page in reader.pages:
        text.append(page.extract_text())
    return "\n".join(text)

def extract_text_from_docx(file):
    doc = Document(file)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return "\n".join(text)

