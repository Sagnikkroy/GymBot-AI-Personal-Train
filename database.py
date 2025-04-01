import sqlite3

def init_db():
    conn = sqlite3.connect('users.db')  # Create a SQLite database file
    c = conn.cursor()

    # Create table for storing user information
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
