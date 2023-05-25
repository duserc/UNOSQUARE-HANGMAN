from flask import Flask
from flask import request, jsonify
import random 

app = Flask(__name__)

game_id = 1
unmaskedword = "string"

words = {
    "ALGORITHM": 1,
    "VARIABLE": 2,
    "FUNCTION": 3,
    "DEBUGGING": 4,
    "COMPILER": 5
}

game = {
    "masked word": "null",
    "Remaining attempts": 6,
    "Guesses so far": [],
    "Game status": "in progress"
}

# Initialize a new game with a new word and return a game ID, aswell as masking the current word
@app.route("/games/", methods=["POST"])
def games():
    global game_id
    global game
    game_id = random.randint(1,5)
    for word in words:
        if words[word] == game_id:
            global unmaskedword
            unmaskedword = word
    maskedword = "_" * len(unmaskedword)
    game["masked word"] = maskedword
    game["Game status"] = "in progress"
    return jsonify(game_id), 201

# gamepos outputs game dict using game_id, also handles deleting current game
@app.route("/games/<game_id>", methods=["GET","DELETE"])
def gamepos(game_id):
    global game
    if request.method == "GET":
        return jsonify(game), 200
    
    if request.method == "DELETE":
        del words[unmaskedword]
        game["Game status"] = "deleted"
        return jsonify({"Message": "Game deleted"}), 204

@app.route("/games/<game_id>/guesses", methods=["POST"])
def guesses(game_id):
    #checks if game is in progress
    if game["Game status"] != "in progress":
        return jsonify({"Error": "Game not in progress"}), 404

    global unmaskedword
    data = request.get_json()
    letter = data["letter"]
    #edge case protection: lower and uppercase accepted
    letter = letter.upper()

    # edge-case: ensuring no repeated guesses
    if letter in game["Guesses so far"]:
        return jsonify({"Error": "Letter already guessed"}, game), 409
    else:
        # stores guessed letters
        game["Guesses so far"].append(letter)
        unmaskedword = list(unmaskedword)

        global j
        j=0
        global correct_counter
        correct_counter = 0

        # checking for matching letters in hangman word
        for i in unmaskedword:
            j+=1
            if i == letter:
                # replacing "_" with guessed letter
                new_word = game["masked word"]
                new_word = list(new_word)
                new_word[j-1] = letter
                new_word = "".join(map(str,new_word))
                game["masked word"] = new_word

                # check if word is fully guessed, congratulating and returning 200 if so
                missing_letter = 0
                for i in new_word:
                    if i == "_":
                        missing_letter+=1
                if missing_letter == 0:
                    game["Game status"] = "won"
                    return jsonify({"Message": "Congratulations! You have guessed the word correctly."}, game), 200
                correct_counter +=1

            # if letter is incorrectly guessed, reduce lives
            if j == len(unmaskedword) and correct_counter == 0:
                if game["Remaining attempts"] > 1:
                    game["Remaining attempts"]-=1
                    return jsonify({"Wrong letter":"Try again"}, game), 400
                else:
                    # if no more lives left, game over
                    game["Remaining attempts"]-=1
                    game["Game status"] = "lost"
                    return jsonify({"Error": "No more attempts left, game over"}, game), 422
                
        # letter is correctly guessed
        return jsonify({"Welldone":"Guess again!"}, game), 201

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=4567)