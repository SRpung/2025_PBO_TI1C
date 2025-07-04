import sqlite3
from konfigurasi import DB_NAME

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL)
                    ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS skills (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        category TEXT,
                        user_id INTEGER,
                        FOREIGN KEY(user_id) REFERENCES users(id))
                    ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS progress (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        skill_id INTEGER,
                        date TEXT,
                        description TEXT,
                        duration INTEGER,
                        level INTEGER,
                        FOREIGN KEY(skill_id) REFERENCES skills(id))
                    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
