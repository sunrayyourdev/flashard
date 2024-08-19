
import sys
import os
from unittest import TestCase, main
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from models.Card import Card

class TestCard(TestCase):

    def setUp(self):
        self.card = Card(0, "Front Text", "Back Text")

    def test_get_front(self):
        self.assertEqual(self.card.get_front(), "Front Text")

    def test_set_front(self):
        self.card.set_front("New Front Text")
        self.assertEqual(self.card.get_front(), "New Front Text")

    def test_get_back(self):
        self.assertEqual(self.card.get_back(), "Back Text")

    def test_set_back(self):
        self.card.set_back("New Back Text")
        self.assertEqual(self.card.get_back(), "New Back Text")

    def test_get_rating(self):
        self.assertEqual(self.card.get_rating(), 0)

    def test_set_rating_valid(self):
        self.card.set_rating(3)
        self.assertEqual(self.card.get_rating(), 3)

    def test_set_rating_invalid(self):
        with self.assertRaises(ValueError):
            self.card.set_rating(5)
        self.assertEqual(self.card.get_rating(), 0)  # Rating should not change
        with self.assertRaises(ValueError):
            self.card.set_rating(-1)
        self.assertEqual(self.card.get_rating(), 0)  # Rating should not change


if __name__ == "__main__":
    main()