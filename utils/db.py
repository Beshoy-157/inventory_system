import sqlite3

def connect():
    return sqlite3.connect("database.db")

def init_db():
    conn = connect()
    cursor = conn.cursor()

    # جدول المنتجات
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        name TEXT PRIMARY KEY,
        qty INTEGER
    )
    """)

    # جدول العمليات
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        qty INTEGER,
        type TEXT
    )
    """)

    conn.commit()
    conn.close()