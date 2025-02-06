import base64
import io
import os

import google.generativeai as genai
import pdf2image
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))


# ------------------FUNCTIONS------------------

def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input_text, pdf_content[0], prompt])
    return response.text


def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format="JPEG")
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")


# ------------------UI------------------------

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text = st.text_area("Enter the job description", key="input")
uploaded_file = st.file_uploader("Upload your resume in PDF format", type=["pdf"])
if uploaded_file is not None:
    st.write("PDF uploaded successfully")

submit1 = st.button("Tell me about the resume")
submit2 = st.button("How can I Improvise my skills")
submit3 = st.button("Percentage match")

input_prompt="""
You are an experienced HR with Tech Experience in the field of data science,
big Data engineering, your task is to review the provided resume against the job description.
Please share your professional evaluation on whether the candidate's profile align with this
"""

