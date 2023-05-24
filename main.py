from flask import Flask
from flask import request, jsonify
import random 

app = Flask(__name__)



# Dictionary of KEY: potential hangman words, VALUE: gameID
words = {
    "ALGORITHM": 1,
    "CODE": 2,
    "DEBUG": 3,
    "FUNCTION": 4,
    "VARIABLE": 5
}

#initialize gameid for gamepos
game_id = 1
# Initialize a dictionary to store game status
game = {
    "masked word": "null",
    "Remaining attempts": 6,
    "Guesses so far": [],
    "Game status": "in progress"
}

# Initialize an empty list to store incorrect guesses
incorrectGuesses = []
correctGuesses = []
#intialize string to store og word without the "_"
unmaskedword = "string"




# Initialize a new game with a word and return a game ID, aswell as masking the current word
@app.route("/games/", methods=["POST"])
def games():
    global game_id
    game_id = random.randint(1,5)
    for word in words:
        if words[word] == game_id:
            global unmaskedword
            unmaskedword = word
    maskedword = "_" * len(unmaskedword)
    game["masked word"] = maskedword
    return jsonify(game_id), 201

@app.route("/games/<game_id>", methods=["GET"])
def gamepos(game_id):
    return jsonify(game), 201

@app.route("/games/<game_id>/guesses", methods=["POST"])
def guesses(game_id):
    global unmaskedword
    data = request.get_json()
    letter = data["letter"]
    letter.upper()
    if letter in game["Guesses so far"]:
        return jsonify({"error": "letter already guessed"}, game), 409
    else:
        # Loops every letter checking for matches. If match = replace "_" with the letter.
        # no match = adjusted score, potential game over. 409
        # saves chosen letter - no double votes
        game["Guesses so far"].append(letter)
        unmaskedword = list(unmaskedword)

        global j
        j=0
        global correct_counter
        correct_counter = 0

        for i in unmaskedword:
            j+=1
            if i == letter:
                # replacing "_" with letter
                new_word = game["masked word"]
                new_word = list(new_word)
                new_word[i] == letter
                game["masked word"] = new_word

                # check if word is guessed
                missing_letter = 0
                for i in new_word:
                    if i == "_":
                        missing_letter+=1
                if missing_letter == 0:
                    game["Game status"] = "won"
                    return jsonify({"message": "Congratulations! You have guessed the word correctly."}, game), 200

                correctGuesses.append(letter)
                correct_counter +=1
            if j == len(unmaskedword) and correct_counter == 0:
                incorrectGuesses.append(letter)
                if game["Remaining attempts"] > 1:
                    game["Remaining attempts"]-=1
                    return jsonify({"wrong letter":"try again"}, game), 201
                else:
                    game["Remaining attempts"]-=1
                    game["Game status"] = "lost"
                    return jsonify({"error": "No more attempts left, game over"}, game), 409
                
            return jsonify(game)
            
            

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=4567)