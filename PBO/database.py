import sqlite3
from konfigurasi import DB_NAME

class Database:

    def insert_user(self, name):
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute("INSERT INTO users (name) VALUES (?)", (name,))
            conn.commit()

    def insert_skill(self, name, category, user_id):
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute("INSERT INTO skills (name, category, user_id) VALUES (?, ?, ?)",
                         (name, category, user_id))
            conn.commit()

    def insert_progress(self, skill_id, date, description, duration, level):
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute("INSERT INTO progress (skill_id, date, description, duration, level) VALUES (?, ?, ?, ?, ?)",
                         (skill_id, date, description, duration, level))
            conn.commit()

    def get_users(self):
        with sqlite3.connect(DB_NAME) as conn:
            return conn.execute("SELECT * FROM users").fetchall()

    def get_skills(self, user_id):
        with sqlite3.connect(DB_NAME) as conn:
            return conn.execute("SELECT * FROM skills WHERE user_id = ?", (user_id,)).fetchall()

    def get_progress(self, skill_id):
        with sqlite3.connect(DB_NAME) as conn:
            return conn.execute("SELECT * FROM progress WHERE skill_id = ?", (skill_id,)).fetchall()
