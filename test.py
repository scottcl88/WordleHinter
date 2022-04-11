import unittest
from unittest.mock import patch
from logic import Logic
from main import User


class TestSum(unittest.TestCase):

    def test_load(self):
        logic = Logic()
        logic.load()
        self.assertEqual(len(logic.word_list), 2309, "Should have 2309 words")

    def test_get_letters(self):
        logic = Logic()
        user = User(logic)
        with patch('builtins.input', return_value='abcde') as mock_input:
            user.get_letters()
        mock_input.assert_called_once()
        self.assertNotEqual(user.known_word, "abcde", "Should have a known word")
        self.assertEqual(len(user.known_word), 5, "Should have 5 characters")

    def test_get_known_letters(self):
        logic = Logic()
        user = User(logic)
        user_input = [
            'abcde',
            'xyz',
        ]
        with patch('builtins.input', side_effect=user_input):
            user.get_known_letters()
        self.assertEqual(user.known_correct_letters, "abcde",
                         "Should have known correct letters")
        self.assertEqual(user.known_wrong_letters, "xyz",
                         "Should have known wrong letters")


if __name__ == '__main__':
    unittest.main()
