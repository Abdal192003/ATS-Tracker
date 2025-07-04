import base64
import io
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image
import fitz  # PyMuPDF
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    # model=genai.GenerativeModel("gemini-pro-vision")
    # model = genai.GenerativeModel("gemini-pro-vision")
    model = genai.GenerativeModel('gemini-1.5-flash')  # or 'gemini-1.5-pro'
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Read the PDF file
        pdf_data = uploaded_file.read()
        
        # Open the PDF with PyMuPDF
        doc = fitz.open(stream=pdf_data, filetype="pdf")
        
        # Convert first page to an image
        page = doc[0]
        pix = page.get_pixmap()
        
        # Convert to PIL Image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Convert to bytes
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file Uploaded")        
    
# Streamlit app

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)....",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1=st.button("Tell Me About Resume")

# submit2=st.button("How Can I Improvise my Skills")

# submit3=st.button("What are the keywords which are missing")

submit3=st.button("Percentage Match")

input_prompt1="""
You are an experienced HR With Tech Experience in the field of Data Science,Full Stack Web
Development,Big Data Engineering,DEVOPS,Data Analyst, your task is to review the provided
resume against the job description for these profiles.
Please share your professional evaluation on whether the candidate's profile aligns with 
the role.Highlight the strength and weaknesses of the applicant in relation to the specified job requirements
"""

input_prompt3="""
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of 
data science,Full Stack Web Development,Big Data Engineering,DEVOPS,Data Analyst
and deep ATS functionality, your task is to evaluate the resume against the provided job description.
give me the percentage of the match if the resume matches job description. First the output should come as percentage and the keywords missing
and last final thoughts.  
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")