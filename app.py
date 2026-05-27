import streamlit as st
import os
from dotenv import load_dotenv
try:    
    load_dotenv()
except Exception as e:
    pass
from src.app_db import init_db, add_record, get_chat_history, get_recent_chat_history, clear_chat_history
from src.intel import generate_response, initialize_token_state
from assets.greetings import get_random_greeting

st.set_page_config(page_title="InfinityAI", page_icon=":sparkles:", layout="wide")

#inject css from styles.css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
script_dir = os.path.dirname(os.path.abspath(__file__))
css_path = os.path.join(script_dir, "assets/style.css")
if not os.path.exists(css_path):
    st.error("CSS file not found.")
else: 
    local_css(css_path)


st.title("InfinityAI - Your AI Companion")
st.caption("") #Will write a caption here later

# Display a random greeting
    


initialize_token_state()

with st.sidebar:
    
    st.header("InfinityAI")
    st.image("assets/logo.png", width=True)

    st.header("Token Usage")
    st.metric("Prompt tokens", st.session_state.prompt_tokens)
    st.metric("Completion tokens", st.session_state.completion_tokens)
    st.metric("Total tokens", st.session_state.total_tokens)

    # dropdown so user can select the model they want to use, for now only gpt-3.5-turbo, but will add more later
    model_options = ["gpt-3.5-turbo"] # Add your favorite models once you clone and add your own API

    with st.expander("About", expanded=False):
        st.markdown(
            """
            **InfinityAI** is evolving from scratch. 
            Right now it has memory and a simple chat experience. 
            I will make it *better* day-by-day and add major features soon.
            """
        )

    selected_model = st.selectbox("Select Model", model_options)

    # clear button
    if st.button("CLEAR HISTORY"):
        clear_chat_history()
        st.session_state.messages = []
        st.success("Chat history cleared successfully!")
    

    
#debug feature, will remvove later
key = os.getenv("OPENAI_API_KEY")
if not key:
    st.error("OPENAI_API_KEY is not set in the environment variables.")
    st.stop()
try:
    init_db()
except Exception as e:
    st.error(f"Error initializing database: {e}")
    st.stop()


## Chat interface with message display

TOKEN_LIMIT = 10000

if "messages" not in st.session_state:
    st.session_state.messages = []

chat_container = st.container()

with chat_container:
    if not st.session_state.messages:
        st.markdown(get_random_greeting(), unsafe_allow_html=True)
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("You:") # restricted for now

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.spinner("Thinking..."):
            if st.session_state.total_tokens > TOKEN_LIMIT:
                response = "Sorry, the conversation has reached the maximum token limit. Please try again a few hours."
            else:
                response = generate_response(user_input, get_recent_chat_history(window_limit=10))
            st.session_state.messages.append({"role": "assistant", "content": response})
            add_record(user_input, response)
            with st.chat_message("assistant"):
                st.markdown(response)
        
        
    with st.expander('Chat History', expanded = False):
        if not get_chat_history():
            st.markdown("Please start a coversation and it wii")
        for user_msg, ai_msgg, timestamp in get_chat_history():
            st.markdown(f"You: {user_msg}")
            st.markdown(f"InfinityAI: {ai_msgg} {timestamp}")


# Major feature: idk