from flask import Flask, g
from flask_cors import CORS

import sqlite3

from modules.getAgeOfCelebrity import get_age_of_celebrity

DATABASE = 'database.db'

app = Flask(__name__)
cors = CORS(app)

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
    age = get_age_of_celebrity(celebrity[2])
    data = {
        'name': celebrity[1],
        'age': age,
        'gender': celebrity[3],
        'nationality': celebrity[4],
        'occupation': celebrity[5]
    }
    return data

if __name__ == '__main__':
    app.run(debug=True)