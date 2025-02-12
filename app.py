import os

import PyPDF2 as pdf
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))


def get_genai_response(input_text):
    print("input_text", input_text)
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


def generate_prompt(text, jd, type):
    if type == 1:
        input_prompt1 = f"""
        Hey Act Like a skilled or very experience ATS(Application Tracking System)
        with a deep understanding of tech field, software engineering, data science, data analyst
        and big data engineer. your task is to review the provided resume against the job description.
        Please share your professional evaluation on whether the candidate's profile align with the role.
        Highlight the strengths and weaknesses of the applicant in relation to that specified job requirements.
        resume: {text}
        description: {jd}
        """
        return input_prompt1

    elif type == 2:
        input_prompt2 = f"""
        Hey Act Like a skilled or very experience ATS(Application Tracking System)
        with a deep understanding of tech field, software engineering, data science, data analyst
        and big data engineer.
         your role is to scrutinize the resume in light of the job description provided.
         Share your insights on the candidate's suitability for the role from an HR perspective,
         Additionally, offer advice on enhancing the candidate's skills and identify areas of interest
         resume: {text}
        description: {jd}
        """
        return input_prompt2

    elif type == 3:
        input_prompt3 = f"""
        Hey Act Like a skilled or very experience ATS(Application Tracking System)
        with a deep understanding of tech field, software engineering, data science, data analyst
        and big data engineer.
        Your task is to evaluate the resume against the provided job description, give me the percentage of match
        if the resume matches job description. First the output should come as percentage and then keywords missing.
        resume: {text}
        description: {jd}
        """
        return input_prompt3

# ----------------------UI---------------------


st.title("Application Tracking System")
st.text("Improve your Resume ATS")
jd = st.text_area("Paste the job Description")
uploaded_files = st.file_uploader("Upload your resume", type="pdf", help="Please upload resume in pdf format")
submit1 = st.button("Tell me about the resume")
submit2 = st.button("How can I Improvise my skills")
submit3 = st.button("Percentage match")


if submit1:
    if uploaded_files is not None:
        text = input_pdf_text(uploaded_files)
        prompt = generate_prompt(text, jd, 1)
        with st.spinner("Loading..."):
            response = get_genai_response(prompt)
            st.subheader("The Response is :")
            st.write(response)
elif submit2:
    if uploaded_files is not None:
        text = input_pdf_text(uploaded_files)
        prompt = generate_prompt(text, jd, 2)
        with st.spinner("Loading..."):
            response = get_genai_response(prompt)
            st.subheader("The Response is :")
            st.write(response)
elif submit3:
    if uploaded_files is not None:
        text = input_pdf_text(uploaded_files)
        prompt = generate_prompt(text, jd, 3)
        with st.spinner("Loading..."):
            response = get_genai_response(prompt)
            st.subheader("The Response is :")
            st.write(response)