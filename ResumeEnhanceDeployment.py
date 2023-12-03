import streamlit as st
#PyPDF2 to read PDF Files
from PyPDF2 import PdfReader
#for interaction with OpenAI GPT model
import openai
import sys
import os
#aids with the natural language processing
import langchain
from langchain.document_loaders import PyPDFLoader
#used for splitting the text
from langchain.text_splitter import RecursiveCharacterTextSplitter
#used the RecursiveCharacterTextSplitter to split texts into smaller chunks using a recursive charcter based approach

sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = "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"

st.title("Resume Enhancer")
st.subheader("Upload your Resume:")
st.text("By Kwadjo Wusu-Ansah\nand Kwame Afriyie-Buabeng Frimpong")
upload_cv = st.file_uploader("Choose file", type=["pdf"])

#uses the OpenAI GPT-4 model to generate a natural language response based on the prompt given
def get_completion(prompt, model="gpt-4"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

#to fetch user input for a job description
def job_description():
    st.subheader("Enter Job Description:")
    job_description = st.text_area("Paste the job description here:", height=200)
    return job_description

#to fetch the Academic Year of the student
def getYear():
    year_options=["Freshmen", "Sophomore", "Junior", "Senior"]
    year=st.selectbox("Academic Year: ",year_options)
    return year

#processes PDF, extracts texts, splits texts
if upload_cv is not None:
    pdf_bd=PdfReader(upload_cv)
    
    text= " "
    for page in pdf_bd.pages:
        text += page.extract_text()
        
    text_splitter= RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=0,
        length_function=len
    )

    chunks=text_splitter.split_text(text=text)


job_requirements=job_description()

year=getYear()


    

#for output
if st.button("Generate Feedback"):
    #prompt the model obeys
    prompt=f"""

You are a professional resume writer. \
Your task is to read the resume and the job description provided by the user then, \
note down the things that need to be improved based on the general guidelines for good resume writing. \
So checking whether the user's resume meets the requirements of the job description \

Assume the student a {year} in Univeristy

Given the user resume delimited by ```

If the user doesn't input a resume, tell the user  "This is not a resume" \

Remember to:
1. Proofread the user's resume to check if there are spelling, grammatical errors and \
if action verbs are being used at the appropriate places. \
2. Proofread the user's resume to check if the writing in the resume is clear and \
 understandable \
3. Check that the job experience listed in the resume occurred no more than three years ago. \
4. Check whether the user resume uses metrics to quantify the level achievements. \
5. Check for the use for the use of personal pronouns. \
6. Check for consistent formatting. \
7. Check for whether at most 3 bullet points in each experience in the user's resume \

From the notes made, output labeled recommendations as to how the user can improve the resume and examples of how
they can be implemented in the users resume. 
Make the output as helpful as possible to the user to help the user land the job requirements \


User's Resume:```{chunks}```


Requirements:```{job_requirements}`````


"""
    #response that calls the get_completion
    response=get_completion(prompt)
    st.write(response)
    
    






