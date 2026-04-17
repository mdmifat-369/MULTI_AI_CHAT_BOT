from google import genai
from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

api_key=os.getenv("OPEN_AI_KEY")



# API CALLING SECTION********************************************************************

openai_client = OpenAI(
     base_url="https://openrouter.ai/api/v1",
     api_key=os.getenv("KEY")
)

gemini_client = genai.Client(api_key="AIzaSyBG8aF_551QN0uqFsslIYPA0SrT7WOAy_g")

deepseek_client = OpenAI(
     base_url="https://openrouter.ai/api/v1",
     api_key=os.getenv("KEY")
 )

#*****************************************************************************************

def build_combined_prompt(ans1, ans2, ans3):
    combined_prompt = f"""
You are a final answer generator.

You will be given 3 AI answers. Your task:
- Compare them
- Remove mistakes
- Merge best points
- Give ONE final clean answer

---

Answer 1:
{ans1}

Answer 2:
{ans2}

Answer 3:
{ans3}

---

Now give final answer:
"""
    return combined_prompt



# ***************************************************************************************
def chatgpt_answer(text):
    response=openai_client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {"role":"user","content":text}
        ]
    )

    return response.choices[0].message.content

def gemini_answer(text):
        response=gemini_client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=text
        )
        return response.text

def deepseek_answer(text):
    response=deepseek_client.chat.completions.create(
        model="deepseek/deepseek-r1",
        messages=[
            {"role": "user", "content": text}
        ]
    )

    return response.choices[0].message.content