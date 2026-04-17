import streamlit as st
import os
from dotenv import load_dotenv
from api_calling import chatgpt_answer,gemini_answer,deepseek_answer,build_combined_prompt

# front Page
st.title("THOW YOUR QUESTION MY BOT GIVE YOU THE BEST ANSWER")


# sidebar works****************************************************************************
Menu=st.sidebar.selectbox(
    "Menu",
    ["Home","ChatGPT","Gemini","DeepSeek","Best answer"],
    index=None
)

# ******************************************************************************************


# Home Page ***************************
if Menu=="Home":
    st.markdown("""
    <div style="text-align:center;">
        <img src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png" width="220">
        <h1 style="
            font-size:50px;
            font-weight:bold;
            background: linear-gradient(to right, #00c6ff, #0072ff);
            -webkit-background-clip: text;
            color: transparent;
            text-shadow: 0px 0px 20px rgba(0,198,255,0.7);
        ">
        🤖 WELCOME TO MY CHAT BOT
        </h1>
    </div>
""", unsafe_allow_html=True)
    

# best answer section works

if Menu=="Best answer":
    prompt = st.text_input("Ask something:")

    if prompt:
      
      with st.spinner("Please wait All 3 AI Disscussing Your Question and Give You the best ans:"):
          ans1=chatgpt_answer(prompt)
          ans2=gemini_answer(prompt)
          ans3=deepseek_answer(prompt)

          final=gemini_answer(build_combined_prompt(ans1,ans2,ans3))

          st.markdown(final)

elif Menu=="ChatGPT":
    prompt = st.text_input("Ask something:")
    with st.spinner("Please wait......"):
       ans1=chatgpt_answer(prompt)
       st.markdown(ans1)

elif Menu=="Gemini":
    prompt = st.text_input("Ask something:")

    with st.spinner("Please wait..."):
       ans2=gemini_answer(prompt)
       st.markdown(ans2)

elif Menu=="DeepSeek":
    prompt = st.text_input("Ask something:")

    with st.spinner("Please wait..."):
      ans3=deepseek_answer(prompt)
      st.markdown(ans3)









