# Hangman API

This is a simple Hangman API game implemented using Flask and Python. The game allows players to create and retrieve a game, along with modifying the game's state by guessing letters to uncover a hidden word. 

## Installation

1. Clone the repository: 

git clone https://github.com/duserc/Unosquare-Hangman.git

2. Install the required dependencies:

pip install -r requirements.txt

## Usage

1. Start the Flask server:

python app.py

2. Create a new game by making a POST request to "/games/" endpoint, I used postman below:

![Screenshot of exact postman input used to create the game]
(https://imgur.com/a/gnqT68A)

3. This will initialize a new game and return a unique game ID (game_id).

![Screenshot of returned unique game ID - this is between 1 and 5 for readability in this instance]
(https://imgur.com/nSHP7hl)

4. Get the current game state by making a GET request to /games/{game_id} endpoint:

![Screenshot of postman input]
(https://imgur.com/gxl8Qo8)

5. This will retrieve the current game state, including the masked word, remaining attempts, and previous guesses.

![screenshot of returned gamestate]
(https://imgur.com/N4EE9hB)

6. You can also delete a game by making a DELETE request to /games/{game_id} endpoint:

