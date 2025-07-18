import sqlite3

conn= sqlite3.connect("db/email_logs.db", check_same_thread=False)
cursor= conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        subject TEXT,
        intent TEXT,
        status TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )                       
""")
conn.commit()