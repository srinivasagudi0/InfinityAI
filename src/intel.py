import streamlit as st
from openai import OpenAI
from datetime import datetime

client = OpenAI()

def initialize_token_state():
    st.session_state.setdefault("prompt_tokens", 0)
    st.session_state.setdefault("completion_tokens", 0)
    st.session_state.setdefault("total_tokens", 0)


def generate_response(prompt, history):
    initialize_token_state()

    if len(prompt) > 2000:
        st.warning("Your message is too long. Please shorten it to under 2000 characters.")
        return "Sorry, your message is too long. Please shorten it to under 2000 characters."

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

        if response.usage:
            st.session_state.prompt_tokens += response.usage.prompt_tokens
            st.session_state.completion_tokens += response.usage.completion_tokens
            st.session_state.total_tokens += response.usage.total_tokens

        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating response: {e}")

    #too organized, I like it. I will keep it this way.
