from flask import Flask
from controllers.game import mod as game_module
import random 

app = Flask(__name__)

app.register_blueprint(game_module)

# Dictionary of KEY: potential hangman words, VALUE: gameID
words = {
    "ALGORITHM": 1,
    "CODE": 2,
    "DEBUG": 3,
    "FUNCTION": 4,
    "VARIABLE": 5
}

# Initialize a dictionary to store game status
game = {
    "masked word": "null",
    "Remaining attempts": 6,
    "Guesses so far": "null",
    "Game status": "in progress"
}

# Initialize an empty list to store incorrect guesses
incorrectGuesses = []
correctGuesses = []

# Initialize a new game with a word and return a game ID, aswell as masking the current word
@app.route("/games/", methods=["POST"])
def games():
    randomint = random.randint(1,5)
    gameID = randomint
    for word in words:
        if words[word] == gameID:
            unmaskedword = word
    maskedword = "_" * len(unmaskedword)
    game["masked word"] = maskedword
    return gameID

@app.route("/games/<gameID>", methods=["GET"])
def session(gameID):
    return game

@app.route("/games/<gameID>/guesses")
def guesses(gameID):



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=4567)



        
