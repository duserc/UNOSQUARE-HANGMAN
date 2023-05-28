# Hangman API

This is a simple Hangman API game implemented using Flask and Python. The game allows players to create and retrieve a game, along with modifying the game's state by guessing letters to uncover a hidden word. This was created as part of Unosquare's Hangman Game API challenge. Their full readme including all specifications that this code was designed to follow, can be found here:  https://github.com/UnosquareCOE/graduate-challenge/blob/main/README.md

Thank you to Unisquare for the opportunity!

The following code covers all 'stretch' requirements, including full unittest coverage.

Much of the installation guide below was already mentioned in the above Unosquare [README](https://github.com/UnosquareCOE/graduate-challenge/blob/main/README.md). If you dont require installation assistance: [skip to Usage](#usage)

Alternatively goto:

-[installation](#installation)
  -[installingPython&pip](#installing-pythonpip)
  -[clonerepository](#clone-the-repository)
-[Usage](#usage)
-[unittest](#unittest)

To try the game out on your own system, follow these steps:

## Installation

You can [skip](#clone-the-repository) the following installation guide if you have:

- python
- pip

### Installing python&pip

1. download python 3.11+ here:

its good practice to tick the box: `add python .exe to path`

https://www.python.org/downloads/release/python-3113/.

2. PIP

pip should come installed with modern versions of python

- if you dont have it: https://pip.pypa.io/en/stable/installation/

3. Check your python isntallation

- Open terminal/command line

- type `python --version` -  You should see `3.11.3` or similar.

### Clone the repository

if you dont have git installed, click the following link: https://git-scm.com/downloads

inside a terminal, navigate to the directory that you wish to download the API and type: `git clone https://github.com/duserc/Unosquare-Hangman.git` into a terminal.

1. Install the required dependencies:

`pip install -r requirements.txt`

## Usage

To test the API manually via postman, follow this guide. To test via unittest, skip to [unittest](#unittest).

install postman: 

https://www.postman.com/downloads/

select, NEW at the top, then select: `HTTP REQUEST`

1. Start the Flask server:

`python app.py`

2. Create a new game by making a POST request to "http://localhost:4567/games/" endpoint, I used postman below:

<picture>
  <img alt="Screenshot of exact postman input used to create the game" src="https://github.com/duserc/Unosquare-Hangman/blob/main/images/unop/u1.png">
</picture>

This will initialize a new game and return a unique game ID (game_id), returning code 201.

3. Get the current game state by making a GET request to http://localhost:4567/games/{game_id} endpoint:

<picture>
  <img alt="Screenshot of postman input" src="https://github.com/duserc/Unosquare-Hangman/blob/main/images/unop/u2.png">
</picture>

This will retrieve the current game state, including the masked word, remaining attempts, and previous guesses.


6. You can also delete a game by making a DELETE request to http://localhost:4567/games/{game_id} endpoint:

<picture>
  <img alt ="screenshot of delete request" src="https://github.com/duserc/Unosquare-Hangman/blob/main/images/unop/u3.png">
</picture>

Returning the error code of 204.

9. You must create a new game once again, using a POST request to /games once again.

10. When using a GET response to /games/{game_id} we will see that a game is once again in progress. Returning 200.

<picture>
  <img alt="/games/5 with game status currently in progress" src="https://github.com/duserc/Unosquare-Hangman/blob/main/images/unop/u4.png">
</picture>

11. To guess a letter, modify postman 'headers' with the following edits: 

<picture>
  <img alt="Content-Type : application/json, Accept : application/json" src="https://github.com/duserc/Unosquare-Hangman/blob/main/images/unop/u5.png">
</picture>

Submitting a POST request via: http://localhost:4567/games/{game_id}/guesses

12. You can now guess a letter by entering a json input into `body`. I have guessed: `{"letter":"e"}`.

<picture>
  <img alt="Content-Type : application/json, Accept : application/json" src="https://github.com/duserc/Unosquare-Hangman/blob/main/images/unop/u6.png">
</picture>

13. If this letter is not a valid guess, such as: `#` or `@` then the code shall output the following error:
`{"Message": "Guess must be supplied with 1, letter"}`
Also returning the error code: 400 (bad request)

If you are interested in viewing more edgecase coverage, check the test_game.py file inside of the tests folder. Alternatively, check out [unittest](#unittest).

14. If the user chose a correct word this is output: 
`"Message": "Congratulations! You have guessed the word correctly."`
with the response code: 200.

The game state is gradually output as you guess each letter, updating guessed letters, lives left and uncovering letters in the hidden word.

<picture>
  <img alt="Content-Type : application/json, Accept : application/json" src="https://github.com/duserc/Unosquare-Hangman/blob/main/images/unop/u7.png">
</picture>

The above word is "Airport" so we have lost 1 life with the incorrect letter guess of `b`.

## unittest

The code found in `.\controllers\game.py` has full edgecase testcoverage via `.\tests\test_game.py`.

The tests can be ran by executing `python -m unittest` in the root directory.

<picture>
  <img alt="Content-Type : application/json, Accept : application/json" src="https://github.com/duserc/Unosquare-Hangman/blob/main/images/unop/u8.png">
</picture>