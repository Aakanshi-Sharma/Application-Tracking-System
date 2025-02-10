import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))


def get_genai_response(input_text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(input_text)
    return response.text



