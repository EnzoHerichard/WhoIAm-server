import sqlite3
import json

jsonC = 'celebrities.json'

def drop_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    DROP TABLE IF EXISTS celebrities
    ''')
    conn.commit()
    conn.close()

def create_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE celebrities(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    birth TEXT,
    gender TEXT,
    nationality TEXT,
    occupation TEXT
    )
    ''')
    conn.commit()
    conn.close()

def insert_celebrity():
    conn = sqlite3.connect('database.db')

    with open(jsonC) as f:
        celebrities = json.load(f)
        for celebrity in celebrities:
            try:
                conn.execute('''
                INSERT INTO celebrities (name, birth, gender, nationality, occupation) VALUES (?, ?, ?, ?, ?)
                ''', (celebrity['name'], celebrity['birth'], celebrity['gender'], celebrity['nationality'], celebrity['occupation']))
            except sqlite3.IntegrityError as e:
                print(f"Error inserting {celebrity['name']}: {e}")
    conn.commit()
    conn.close()

if __name__ == '__main__':
    drop_db()
    create_db()
    insert_celebrity()
    print('Database created and celebrities inserted')