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
- ~~Token usage counter in session state~~
- ~~Display token usage and cost in the UI~~
- ~~Hard session token limit to prevent runaway costs~~
- ~~Create assets/style.css~~
- ~~Inject css at app startup to make it look nice~~
- ~~Customize the app background~~
- ~~Styled chat bubbles for user and AI messages~~
- ~~Custom font~~ Markdown Backed
- ~~Make everything overall look nice and modern with css~~
- ~~Render assistant messages with markdown support for better formatting~~
- ~~Make this look like a chat app, not just ask a question and get an answer and store it in the history~~
- ~~~[!!!EASY] code block styling, luckily done with the help of the markdown lang~~
- ~~[!!!HARD] syntax highlighting for code blocks in assistant messages~~
*Sidebar Polish*
- App logo + name in sidebar
- ~~Styled clear chat button~~
- ~~Model selector dropdown~~
- Live token + cost display (effeciently)
- ~~Collapsable About section~~
- ~~Add canvas_active flag to session state~~
- ~~colums that become actove when state is true, make it the look good as much as a streamlit browser can support~~
-  Canvas placeholder that is empty and shouldopen when needed to isntead of all times
- Css for canvas panel styling.


# THinking about a major feature, something that stands out

## The Live Canvas (Artifacts).

What it is:
Instead of the bot just typing everything into a standard chat bubble, the screen splits in half.

The left side is your normal chat conversation.

The right side is a dedicated, interactive "whiteboard" or canvas.

Why it's the ultimate "Wow" feature:
It feels alive: When the bot writes code, a recipe, a script, or a webpage, that document automatically flies over to the right panel and updates in real-time.

Instant interaction: The user can click buttons on the canvas to preview a website, copy the text, or download a file instantly.

It fixes the scroll problem: Users don’t have to scroll up through miles of chat text to find what the bot created. The final product is always neatly organized right next to the conversation.

If you build a beautiful, smooth Split-Screen Canvas, your app instantly goes from looking like a weekend hobby project to looking like a premium, professional AI tool.