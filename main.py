from flask import Flask, g
import sqlite3

DATABASE = 'database.db'

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

@app.teardown_appcontext
def close_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route("/random")
def random():
    cur = get_db().cursor()
    cur.execute('SELECT * FROM celebrities ORDER BY RANDOM() LIMIT 1')
    celebrity = cur.fetchone()
    data = {
        'name': celebrity[1],
        'birth': celebrity[2],
        'gender': celebrity[3],
        'nationality': celebrity[4],
    }
    return data

if __name__ == '__main__':
    app.run(debug=True)