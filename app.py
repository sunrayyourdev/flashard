from flask import Flask, render_template, request, redirect, url_for
from models.Card import Card
from models.Deck import Deck
from Forms import DeckForm
import shelve
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    with shelve.open('flashcard.db', 'c') as flashcard_db:
        decks = list(flashcard_db["Decks"].values())
    return render_template('dashboard.html', decks=decks)


@app.route('/new_deck', methods=["GET", "POST"])
def new_deck():
    deck_form = DeckForm(request.form)
    if request.method == "POST":
        with shelve.open('flashcard.db', 'c') as flashcard_db:
            decks = flashcard_db["Decks"]
            deck_id = generate_id(decks)
            deck = Deck(deck_id, deck_form.name.data)
            decks[deck_id] = deck
            flashcard_db["Decks"] = decks
            return redirect(url_for('dashboard'))
    else:
        return render_template('new_deck.html', deck_form=deck_form)


# TODO: Change url to use parameter query containing deck_id to GET
@app.route('/deck', methods=["GET", "PUT"])
def deck():
    deck_form = DeckForm(request.form)
    if request.method == "PUT":
        pass
    else:
        return render_template('new_deck.html', deck_form=deck_form, deck={})


# Card Routes
@app.route('/add-card')
def add_card():
    return render_template('add_card.html')


def generate_id(d: dict) -> int:
    """returns the last key of a dict +1"""
    if not d:
        return 1
    last_deck_id = list(d.keys())[-1]
    return last_deck_id + 1


if __name__ == '__main__':
    try:
        with shelve.open('flashcard.db', 'c') as flashcard_database:
            if not flashcard_database:
                flashcard_database["Decks"] = {}
    except IOError as e:
        print(e)
    app.run(debug=True)