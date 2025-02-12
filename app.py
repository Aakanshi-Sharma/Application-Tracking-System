import os

import PyPDF2 as pdf
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))


def get_genai_response(input_text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(input_text)
    return response.text


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
        text += " "
    return text


input_prompt = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field, software engineering, data science, data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide
best assistance for improving the resumes. Assign the percentage Matching based
on JD and missing keywords with high accuracy.
resume: {text}
description: {jd}
I want the response in one single string having the structure
{{"JD Match": "%", "MissingKeywords:[]", "Profile Summary":""}}
"""

# ----------------------UI---------------------


st.title("Application Tracking System")
st.text("Improve your Resume ATS")
jd = st.text_area("Paste the job Description")
uploaded_files = st.file_uploader("Upload your resume", type="pdf", help="Please upload resume in pdf format")
submit_button = st.button("Submit")
if submit_button:
    if uploaded_files is not None:
        text = input_pdf_text(uploaded_files)
        with st.spinner("Loading..."):
            response = get_genai_response(input_prompt)
            st.subheader("The Response is :")
            st.text(response)
