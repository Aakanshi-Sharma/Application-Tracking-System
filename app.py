import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import pdf2image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

# ------------------UI------------------------

st.text_input("Enter the job description...")
