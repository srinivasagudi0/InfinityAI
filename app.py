import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.set_page_config(page_title="My Streamlit App", page_icon=":sparkles:", layout="wide")

st.title("InfinityAI - Your AI Companion")
st.caption("") #Will write a caption here later

key = os.getenv("OPENAI_API_KEY")

if not key:
    st.error("OPENAI_API_KEY is not set in the environment variables.")
else:
    st.success("OPENAI_API_KEY is set successfully.")

client = OpenAI()

def generate_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # I dont want to waste my tokens on gpt-4, so I am using gpt-3.5-turbo for now
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating response: {e}")

# basic chat interface
st.header("Chat with InfinityAI")

user_input = st.text_input("You:", key="user_input")
if st.button("Send", key="send_button"):
    if user_input:
        response = generate_response(user_input)
        st.markdown(f"**InfinityAI:** {response}")
    else:
        st.warning("Please enter a message to send.")