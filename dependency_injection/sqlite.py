import sqlite3
from fastapi import FastAPI, Depends, Header, HTTPException, Request

# db connection
conn = sqlite3.connect('example.db',check_same_thread=False)

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
              (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,
              email TEXT NOT NULL UNIQUE)''')

conn.commit()


app = FastAPI()

@app.get("/users")
def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    if len(users) == 0:
        raise HTTPException(status_code=404, detail="No users found")
    return {"users": users}

 
