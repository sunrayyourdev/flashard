import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from unittest import TestCase, main
from database_functions import generate_id

class TestGenerateId(TestCase):
    def test_generate_id_normal_case(self):
        d = {1: 'deck1', 2: 'deck2', 3: 'deck3'}
        self.assertEqual(generate_id(d), 4)

    def test_generate_id_empty_dict(self):
        d = {}
        with self.assertRaises(IndexError):
            generate_id(d)

    def test_generate_id_invalid_argument(self):
        d = "not a dict"
        with self.assertRaises(AttributeError):
            generate_id(d)

if __name__ == '__main__':
    main()

