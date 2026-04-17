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

if Menu == "Best answer":
    prompt = st.text_input("Ask something:")

    if prompt:
        with st.spinner("3 AI are discussing your question..."):
            
            def safe_call(func, prompt):
                try:
                    return func(prompt)
                except Exception as e:
                    return f"ERROR: {str(e)}"

            ans1 = safe_call(chatgpt_answer, prompt)
            ans2 = safe_call(gemini_answer, prompt)
            ans3 = safe_call(deepseek_answer, prompt)

            if "ERROR" in ans1 or "ERROR" in ans2 or "ERROR" in ans3:
                st.error("LIMIT FINISH")
            else:
                combined_text = build_combined_prompt(ans1, ans2, ans3)

                final = safe_call(gemini_answer, combined_text)

                if "ERROR" in final:
                    final = safe_call(chatgpt_answer, combined_text)

                if "ERROR" in final:
                    st.error("Final summary failed!")
                else:
                    st.markdown(final)

elif Menu == "ChatGPT":
    prompt = st.text_input("Ask something:")

    if prompt:
        with st.spinner("Please wait......"):
            
            try:
                ans1 = chatgpt_answer(prompt)

                if not ans1:
                    st.error("⚠️ Empty response!")
                else:
                    st.markdown(ans1)

            except Exception as e:
                error_msg = str(e)

                if "429" in error_msg:
                    st.error("🚨 LIMIT FINISHED")
                else:
                    st.error(f"❌ Error: {error_msg}")

elif Menu == "Gemini":
    prompt = st.text_input("Ask something:")

    if prompt:
        with st.spinner("Please wait..."):
            try:
                ans2 = gemini_answer(prompt)

                if not ans2:
                    st.error("⚠️ Empty response!")
                else:
                    st.markdown(ans2)

            except Exception as e:
                error_msg = str(e)

                if "429" in error_msg:
                    st.error("🚨 LIMIT FINISHED")
                else:
                    st.error(f"❌ Error: {error_msg}")

elif Menu == "DeepSeek":
    prompt = st.text_input("Ask something:")

    if prompt:
        with st.spinner("Please wait..."):
            try:
                ans3 = deepseek_answer(prompt)

                if not ans3:
                    st.error("⚠️ Empty response!")
                else:
                    st.markdown(ans3)

            except Exception as e:
                error_msg = str(e)

                if "429" in error_msg:
                    st.error("🚨 LIMIT FINISHED")
                else:
                    st.error(f"❌ Error: {error_msg}")









