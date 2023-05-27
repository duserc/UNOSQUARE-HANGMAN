import unittest
import uuid

from flask import jsonify
from main import app
from unittest.mock import patch
from controllers.game import start_game
from controllers.game import get_game_state
from controllers.game import generate_word


GAMEID = "06335e84-2872-4914-8c5d-3ed07d2a2f16"
BANANA = "Banana"

def mock_uuid():
    return uuid.UUID(GAMEID)

def mock_generate_word():
    return BANANA

class TestGameController(unittest.TestCase):

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



if __name__ == '__main__':
    unittest.main()