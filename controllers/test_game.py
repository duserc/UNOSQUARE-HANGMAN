import unittest
import uuid
import json
import controllers.game as game

from flask import Flask
from unittest.mock import patch

GAMEID = "06335e84-2872-4914-8c5d-3ed07d2a2f16"

def mock_uuid():
    return uuid.UUID(GAMEID)

class TestGameController(unittest.TestCase):

    @patch('uuid.uuid4', mock_uuid)
    def test_create_game_returns_valid_id(self):
        id, code = game.start_game()
        self.assertEqual(code, 201)
        self.assertEqual(id, GAMEID)



if __name__ == '__main__':
    unittest.main()