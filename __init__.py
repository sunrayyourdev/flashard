from flask import Flask, render_template
from models.Card import Card
import shelve
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


# TODO: Creates routes for card CRUD


if __name__ == '__main__':
    with shelve.open('flashcard.db', 'c') as flashcard_database:
        if not flashcard_database:
            flashcard_database["Decks"] = {}  # temp database to test card routes
            # flashcard_database["Users"] = {}
    app.run(debug=True)