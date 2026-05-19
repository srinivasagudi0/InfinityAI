import sqlite3

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

def add_record(user_message, ai_response):  
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute(
        '''
        INSERT INTO chat_history (user_message, ai_response) VALUES (?, ?)
        ''', (user_message, ai_response)
    )
    conn.commit()
    conn.close()

def get_chat_history():
    c = sqlite3.connect('chat_history.db').cursor()
    c.execute(""" SELECT user_message, ai_response, timestamp
            FROM chat_history ORDER BY timestamp DESC
              """)
    history = c.fetchall()
    c.connection.close()
    return history

def get_recent_chat_history(window_limit=10):
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute(""" SELECT user_message, ai_response, timestamp
            FROM chat_history ORDER BY timestamp DESC LIMIT ?
              """, (window_limit,))
    history = c.fetchall()
    c.connection.close()
    return history
