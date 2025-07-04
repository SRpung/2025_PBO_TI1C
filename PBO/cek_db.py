import sqlite3

conn = sqlite3.connect("skillforge.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tabel dalam database:")
for table in cursor.fetchall():
    print("-", table[0])

conn.close()
