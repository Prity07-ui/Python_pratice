#sqlite3

import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS student(id INTEGER, name TEXT)"
)

cursor.execute(
    "INSERT INTO student VALUES(1, 'Rahul')"
)

conn.commit()
conn.close()

print("Data Inserted")