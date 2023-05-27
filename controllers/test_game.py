import unittest
import uuid

from flask import jsonify
from main import app
from unittest.mock import patch
from controllers.game import start_game
from controllers.game import get_game_state
from controllers.game import generate_word
from controllers.game import mask_word
from controllers.game import is_valid_guess
from controllers.game import is_correct_guess

GAMEID = "06335e84-2872-4914-8c5d-3ed07d2a2f16"
BANANA = "Banana"

def mock_uuid():
    return uuid.UUID(GAMEID)

def mock_generate_word():
    return BANANA

class TestGameController(unittest.TestCase):

    def test_generate_word_gives_string(self):
        result = generate_word()
        word_list = ["Banana","Canine","Unosquare","Airport"]
        self.assertIn(result, word_list)
        
    def test_masking_mask_word(self):
        word = "Banana"
        guessed_letters = []
        masked_word = mask_word(word, guessed_letters)
        self.assertEqual(masked_word, ['_', '_', '_', '_', '_', '_'])
    
    def test_is_invalid_guess_valid_lower_case(self):
        guess = "a"
        game = "null"
        guess_attempt = is_valid_guess(guess, game)
        self.assertTrue(guess_attempt)
    
    def test_is_invalid_guess_valid_upper_case(self):
        guess = "B"
        game = "null"
        guess_attempt = is_valid_guess(guess, game)
        self.assertTrue(guess_attempt)   
        
    def test_is_invalid_guess_invalid_character(self):
        guess = "#"
        game = "null"
        guess_attempt = is_valid_guess(guess, game)
        self.assertFalse(guess_attempt)

    def test_is_invalid_guess_invalid_len(self):
        guess = "aa"
        game = "null"
        guess_attempt = is_valid_guess(guess, game)
        self.assertFalse(guess_attempt)

    def test_is_invalid_guess_invalid_len(self):
        guess = "aA"
        game = "null"
        guess_attempt = is_valid_guess(guess, game)
        self.assertFalse(guess_attempt)
        
    def test_is_correct_guess_correct(self):
        guess = "a"
        word = "Banana"
        game =  {
        "word": word,
        "guessed_letters": [],
        "attempts": 6,
        "game_status": "waiting first guess"
        }
        is_correct_guess(guess, game, word)
        self.assertEqual(game["guessed_letters"], ["a"])
        self.assertEqual(game["attempts"], 6)
        
    def test_is_correct_guess_incorrect(self):
        guess = "x"
        word = "Banana"
        game =  {
        "word": word,
        "guessed_letters": [],
        "attempts": 6,
        "game_status": "waiting first guess"
        }
        is_correct_guess(guess, game, word)
        self.assertEqual(game["guessed_letters"], ["x"])
        self.assertEqual(game["attempts"], 5)
        
    def test_is_correct_guess_incorrect(self):
        guess = "u"
        word = "Unosquare"
        game =  {
        "word": word,
        "guessed_letters": [],
        "attempts": 6,
        "game_status": "waiting first guess"
        }
        is_correct_guess(guess, game, word)
        self.assertEqual(game["guessed_letters"], ["u"])
        self.assertEqual(game["attempts"], 6)
        

    
    @patch('controllers.game.generate_word', mock_generate_word)
    @patch('uuid.uuid4', mock_uuid)
    def test_create_game_returns_valid_id(self):
        id, code = start_game()
        self.assertEqual(code, 201)
        self.assertEqual(id, GAMEID)
        
    @patch('controllers.game.generate_word', mock_generate_word)
    @patch('uuid.uuid4', mock_uuid)    
    def test_generate_word_returns_word(self):
        id, code = start_game()
        word = mock_generate_word()
        self.assertEqual(code, 201)
        self.assertEqual(id, GAMEID)
        self.assertEqual(word, "Banana") 
    
    @patch('controllers.game.generate_word', mock_generate_word)
    @patch('uuid.uuid4', mock_uuid)
    def test_check_game_state_returns(self):
        id, code = start_game()
        self.assertEqual(code, 201)
        self.assertEqual(id, GAMEID)
        with app.app_context():
            response = get_game_state(id)
            self.assertEqual(response.status_code, 200)
            game = response.json
            word = mock_generate_word()
            self.assertEqual(word, "Banana") 
            self.assertEqual(game, [
            {'guesses_so_far': [],
            'remaining_attempts': 6,
            'status': 'waiting first guess',
            'word': '______'}, 200])
    
    # @patch('controllers.game.generate_word', mock_generate_word)
    # @patch('uuid.uuid4', mock_uuid)        
    # def test_check_lower_case_guesses(self):
    #     id, code = start_game()
    #     self.assertEqual(code, 201)
    #     self.assertEqual(id, GAMEID)
    #     with app.app_context():
    #         response = get_game_state(id)
    #         self.assertEqual(response.status_code, 200)
    #         word = mock_generate_word()
    #         self.assertEqual(word, "Banana")
            


if __name__ == '__main__':
    unittest.main()