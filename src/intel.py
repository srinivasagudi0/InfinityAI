import streamlit as st
from openai import OpenAI
from datetime import datetime

client = OpenAI()

def generate_response(prompt, history):
    try:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        day = datetime.now().strftime("%A")
        
        system_msg = f"You are a helpful assistant. It is {day} and the current time is {time}. Here is the recent chat history: {history}"
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating response: {e}")

    #too organized, I like it. I wil 