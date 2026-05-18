import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="My Streamlit App", page_icon=":sparkles:", layout="wide")

st.title("InfinityAI - Your AI Companion")
st.caption("") #Will write a caption here later

key = os.getenv("OPENAI_API_KEY")
if not key:
    st.error("OPENAI_API_KEY is not set in the environment variables.")
else:
    st.success("OPENAI_API_KEY is set successfully.")
