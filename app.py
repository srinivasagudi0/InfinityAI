import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
import datetime # for time related context
import sqlite3

load_dotenv()

st.set_page_config(page_title="My Streamlit App", page_icon=":sparkles:", layout="wide")

st.title("InfinityAI - Your AI Companion")
st.caption("") #Will write a caption here later

key = os.getenv("OPENAI_API_KEY")

def init_db():
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT,
            ai_response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def add_record(user_message, ai_response):
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO chat_history (user_message, ai_response) VALUES (?, ?)
    ''', (user_message, ai_response))
    conn.commit()
    conn.close()

def get_chat_history():
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute('SELECT user_message, ai_response, timestamp FROM chat_history ORDER BY timestamp DESC')
    history = c.fetchall()
    conn.close()
    return history

def get_recent_chat_history(window_limit=10):
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute('SELECT user_message, ai_response, timestamp FROM chat_history ORDER BY timestamp DESC LIMIT ?', (window_limit,))
    history = c.fetchall()
    conn.close()
    return history

if not key:
    st.error("OPENAI_API_KEY is not set in the environment variables.")
else:
    st.success("OPENAI_API_KEY is set successfully.")

client = OpenAI()

def generate_response(prompt, history): # for now I am sending all history, but I will implement a better way to send only relevant history later
    try:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        day = datetime.datetime.now().strftime("%A")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # I dont want to waste my tokens on gpt-4, so I am using gpt-3.5-turbo for now
            messages=[
                {"role": "system", "content": "You are a helpful assistant." + f" It is {day} and the current time is {time}." + " Here is the recent chat history: " + str(history)},
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

