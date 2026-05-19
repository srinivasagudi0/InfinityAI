import streamlit as st
import os
from dotenv import load_dotenv
from src.app_db import init_db, add_record, get_chat_history, get_recent_chat_history
from src.intel import generate_response

try:    
    load_dotenv()
except Exception as e:
    pass

st.set_page_config(page_title="My Streamlit App", page_icon=":sparkles:", layout="wide")

st.title("InfinityAI - Your AI Companion")
st.caption("") #Will write a caption here later

#debug feature, will remvove later
key = os.getenv("OPENAI_API_KEY")
if not key:
    st.error("OPENAI_API_KEY is not set in the environment variables.")
else:
    st.success("OPENAI_API_KEY is set successfully.")
try:
    init_db()
except Exception as e:
    st.error(f"Error initializing database: {e}")

# basic chat interface
st.header("Chat with InfinityAI")

user_input = st.text_input("You:", key="user_input")
if st.button("Send", key="send_button"):
    if user_input:

        history = get_recent_chat_history(window_limit=10)
        response = generate_response(user_input, history)
        add_record(user_input, response)
        st.markdown(f"**InfinityAI:** {response}")
    else:
        st.warning("Please enter a message to send.")

# Display chat history
st.header("Chat History")
for user_msg, ai_msg, timestamp in get_chat_history():
    st.markdown(f"**You:** {user_msg}")
    st.markdown(f"**InfinityAI:** {ai_msg} ({timestamp})")
