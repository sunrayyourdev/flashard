import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from unittest import TestCase, main
from models.Deck import Deck
from models.Card import Card


class TestDeck(TestCase):

    def setUp(self):
        self.deck = Deck(1, "Test Deck")

    def test_deck_initialization(self):
        self.assertEqual(self.deck.deck_id, 1)
        self.assertEqual(self.deck.name, "Test Deck")
        self.assertEqual(len(self.deck), 0)

    def test_rename_deck(self):
        self.deck.rename("Renamed Deck")
        self.assertEqual(self.deck.name, "Renamed Deck")

    def test_add_cards(self):
        self.deck.cards = {1: "Card 1", 2: "Card 2"}
        self.assertEqual(len(self.deck), 2)
        self.assertEqual(self.deck.cards[1], "Card 1")
        self.assertEqual(self.deck.cards[2], "Card 2")

    def test_repr(self):
        self.deck.cards = {1: "Card 1"}
        self.assertEqual(repr(self.deck), "Deck(Test Deck, 1)")

    def test_str(self):
        self.deck.cards = {1: "Card 1"}
        self.assertEqual(str(self.deck), "Deck containing 1 card")
        self.deck.cards = {1: "Card 1", 2: "Card 2"}
        self.assertEqual(str(self.deck), "Deck containing 2 card(s)")


if __name__ == "__main__":
    main()