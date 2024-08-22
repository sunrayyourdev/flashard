import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from unittest import TestCase, main
from models.Card import Card


class TestCard(TestCase):

    def setUp(self):
        self.card = Card(0, "Front Text", "Back Text")

    def test_get_front(self):
        self.assertEqual(self.card.front, "Front Text")

    def test_set_front(self):
        self.card.front = "New Front Text"
        self.assertEqual(self.card.front, "New Front Text")

    def test_get_back(self):
        self.assertEqual(self.card.back, "Back Text")

    def test_set_back(self):
        self.card.back = "New Back Text"
        self.assertEqual(self.card.back, "New Back Text")

    # def test_get_rating(self):
    #     self.assertEqual(self.card.rating, 0)

    # def test_set_rating_valid(self):
    #     self.card.rating = 3
    #     self.assertEqual(self.card.rating, 3)

    # def test_set_rating_invalid(self):
    #     with self.assertRaises(ValueError):
    #         self.card.rating = 5
    #     self.assertEqual(self.card.rating, 0)  # Rating should not change
    #     with self.assertRaises(ValueError):
    #         self.card.rating = -1
    #     self.assertEqual(self.card.rating, 0)  # Rating should not change


if __name__ == "__main__":
    main()