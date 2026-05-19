# *Plan*  - What I will do and probably how I will do it

will commit after each step.

- ~~init-repo~~
- ~~set up all the docs such as devlog folder + plan~~
- ~~Bare Streamlit app~~
- ~~.env + config loader~~
- ~~Readme (Barely will come back to this later).~~
- ~~OpenAI client wrapper~~
- ~~Add requirements.txt~~
- ~~basic Chat UI~~
- ~~Wire input -> LLM -> Display~~
- ~~Smoke test~~
- ~~Sqlite connection + Session Store - save chat to a db so they dont dissapear after refresh or new start.~~
- ~~Thread history - send `all` the messages from the conversation to the LLM so it can understand the context of the conversation.~~
- ~~Sliding window truncation - Only send the last few messages to the AI (to save money on API calls); GOOD Word to know BTW.~~
- ~~Make the system organized~~
- ~~Make everything error proof~~
- ~~System prompt management in a file with persona, boundaries, tone, etc.~~
- ~~Graceful error handling and display in the UI~~
- ~~Input length guard to prevent sending too long messages to the API~~
- Token usage counter in session state
- Display token usage and cost in the UI
- Hard session token limit to prevent runaway costs
- Model fallback on Api errors (e.g. if gpt-4 is unavailable, fallback to gpt-3.5)