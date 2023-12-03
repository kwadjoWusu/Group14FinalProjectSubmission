# Group14FinalProjectSubmission

## **Resume Enhancer**

> This project is a resume recommendations application that takes a user's resume and the specific job listing the person is going for. Then our application recommendes way the user can improve their resume.

### It uses the following rules in the prompt to determine the type of recommendations it provides to the user:

> - Check if there are spelling, grammatical errors and 
if action verbs are being used at the appropriate places. 
> - Check if the writing in the resume is clear and 
 understandable 
> - Check that the job experience listed in the resume occurred no more than three years ago. 
> - Check whether metrics were use to quantify the level achievements. 
> - Check for the use of personal pronouns. 
> - Check for consistent formatting. 
> - Check for whether at most 3 bullet points were used in each experience in the user's resume

This project made use of the gpt 4 model pre-trained model with the prompt tailored to the task of resume recommendations.


## How to Host on Your Local Server

### Prerequisites

The project requires a Python setup

### Installation Into Your Python Environment

`
pip install streamlit
`
`
pip install PyPDF2
`
`
pip install openai
`
`
pip install langchain
`

> ** Note that you would need to pay for an API key from OPENAI in order to run the gpt-4 model **
The variable openai.api_key has to be modified to your API key.
> ** URL : ** [openai-api key](https://platform.openai.com/api-keys)
