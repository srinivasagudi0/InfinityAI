import streamlit as st
from openai import OpenAI
from datetime import datetime

client = OpenAI()

def generate_response(prompt, history):
    try:
        with open("system_prompt.txt", "r") as f:
            system_prompt = f.read()
        
    except Exception as e:
        st.error(f"Error loading system prompt: {e}")
        system_prompt = "You are a helpful assistant."

    try:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        day = datetime.now().strftime("%A")
        
        system_msg = f"{system_prompt}\nCurrent time: {time}\nCurrent day: {day}\nChat history:\n{history}"
        
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

    #too organized, I like it. I will keep it this way.