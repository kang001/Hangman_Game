import random
import unittest
from unittest.mock import patch
from hangman_game import hangman

class TestGame(unittest.TestCase):

    @patch('builtins.input', side_effect=[a,b,e,u])
    @patch('builtins.print')
    def test_user_input(self, mock_print, mock_input): #this should test user input by mocking a user input letter, but unsure of how to
        hangman.GetRandomWord()
        self.assert_called_with(a)

    def test_is_user_input_valid(self):
        self.
    @patch(builtins.input, side_effect=[#LIST OF WORDS FROM FILE])
    def test_random_word(self, mock_input): #is it possible to test for this? Unsure if I am doing this correctly
        self.assertEqual(wordList.words, expected_wordList)

        
