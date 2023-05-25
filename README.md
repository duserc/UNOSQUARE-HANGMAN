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

<picture>
  <img alt="Screenshot of exact postman input used to create the game" src="https://github.com/duserc/Unosquare-hangman/images/unop/p1.png">
</picture>

3. This will initialize a new game and return a unique game ID (game_id), returning code 201.

<picture>
  <img alt="Screenshot of returned unique game ID - this is between 1 and 5 for readability in this instance" src="https://github.com/duserc/Unosquare-hangman/images/unop/p2.png">
</picture>

4. Get the current game state by making a GET request to /games/{game_id} endpoint:

<picture>
  <img alt="Screenshot of postman input" src="https://github.com/duserc/Unosquare-hangman/images/unop/p3.png">
</picture>

5. This will retrieve the current game state, including the masked word, remaining attempts, and previous guesses.

<picture>
  <img alt="screenshot of returned gamestate" src="https://github.com/duserc/Unosquare-hangman/images/unop/p4.png">
</picture>

6. You can also delete a game by making a DELETE request to /games/{game_id} endpoint:

<picture>
  <img alt ="screenshot of delete request" src="https://github.com/duserc/Unosquare-hangman/images/unop/p5.png">
</picture>

7. returning the error code of 204:

<picture>
  <img alt="screenshot of responded error code" src="https://github.com/duserc/Unosquare-hangman/images/unop/p6.png">
</picture>

8. Now when you run /games/{game_id} you will recieve the game status of deleted:

<picture>
  <img alt="game has been deleted:" src="https://github.com/duserc/Unosquare-hangman/images/unop/p7.png">
</picture>

9. So, you must create a new game once again, using a POST request to /games.

10. Now when using a GET response to /games/{game_id} (in this case, 5) we will see that a game is once again in progress. Returning 200.

<picture>
  <img alt="/games/5 with game status currently in progress" src="https://github.com/duserc/Unosquare-hangman/images/unop/p8.png">
</picture>

11. To guess a letter, modify postman 'headers' with the following edits: 

<picture>
  <img alt="Content-Type : application/json, Accept : application/json" src="https://github.com/duserc/Unosquare-hangman/images/unop/p9.png">
</picture>

