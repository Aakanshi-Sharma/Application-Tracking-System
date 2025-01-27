import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import pdf2image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))


# ------------------FUNCTIONS------------------

# def get_gemini_response(input_text, pdf_content, prompt):
#     model = genai.GenerativeModel("gemini-1.5-flash")
#     response = model.generate_content([input_text, pdf_content[0], prompt])
#     return response.text


# ------------------UI------------------------

st.text_input("Enter the job description...")
