from flask import Flask, render_template
from models.Card import Card
from Forms import *
import shelve
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    with shelve.open('flashcard.db', 'c') as flashcard_database:
        if not flashcard_database:
            flashcard_database["Decks"] = {}
            # flashcard_database["Users"] = {}
    app.run(debug=True)