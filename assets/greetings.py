import random

Greetings = [
    {
        "emoji": "🌅",
        "headline": "Good to see you!",
        "subtext": "I'm here to think alongside you - ask me anything, big or small.",
        "suggestion": "Try: *What should I focus on today?*"
    },
    {
        "emoji": "⭐️",
        "headline": "Ready when you are.",
        "subtext": "Whether it's researching, planning, or thinking out loud - let's go!",
        "suggestion": "Try: *Help me brainstorm ideas for...*"
    },
    {
        "emoji": "🧠",
        "headline": "Let's think together.",
        "subtext": "Throw me a hard problem. I work best when the question is interesting",
        "suggestion": "Try: *Explain [topic] like I'm new to it.*"
    },
    {
        "emoji": "📝",
        "headline": "What are you working on?",
        "subtext": "I can draft, edit, summarize, or just give you a second opinion.",
        "suggestion": "Try: *Review this and tell me what's missing*"
    },
    {
        "emoji": "🔍",
        "headline": "Ask me anything.",
        "subtext": "No question is too niche. I'll give you a straight honest answer.",
        "suggestion": "Try: *Whats the difference between X and Y?*"
    },
    {
        "emoji": "💡",
        "headline": "New coversation, fresh start.",
        "subtext": "Try: *I need help with...*,",
        "suggestion": "Try: *I need help with...*"
    },
    {
        "emoji": "🚀",
        "headline": "Let's launch!",
        "subtext": "I'm ready to help you achieve your goals and turn ideas into reality.",
        "suggestion": "Try: *What steps should I take to get started?*"
    },
    {
        "emoji": "🎯",
        "headline": "Focus mode: ON.",
        "subtext": "Let's get things done with clarity and purpose.",
        "suggestion": "Try: *Help me prioritize my tasks for today.*"
    }
]

def get_random_greeting():
    g = random.choice(Greetings)
    return f"""
    <div style="
        text-align: center;
        padding: 2.5rem 2rem;
        margin: 1rem auto 2rem;
        max-width: 520px;
        background: linear-gradient(135deg, rgba(124,111,247,0.08) 0%, rgba(28,32,48,0.6) 100%);
        border: 1px solid rgba(124,111,247,0.2);
        border-radius: 20px;
        backdrop-filter: blur(8px);
    ">
        <div style="font-size: 2.4rem; margin-bottom: 12px; line-height:1;">{g['emoji']}</div>
        <h2 style="
            font-size: 1.5rem;
            font-weight: 600;
            color: #eaedf5;
            margin: 0 0 8px;
            font-family: 'DM Sans', sans-serif;
        ">{g['headline']}</h2>
        <p style="
            font-size: 15px;
            color: #8b90a8;
            margin: 0 0 16px;
            line-height: 1.6;
            font-family: 'DM Sans', sans-serif;
        ">{g['subtext']}</p>
        <p style="
            font-size: 13px;
            color: rgba(124,111,247,0.8);
            margin: 0;
            font-style: italic;
            font-family: 'DM Sans', sans-serif;
        ">{g['suggestion']}</p>
    </div>
    """