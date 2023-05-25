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
(https://imgur.com/eXzV75L)

3. This will initialize a new game and return a unique game ID (game_id), returning code 201.

![Screenshot of returned unique game ID - this is between 1 and 5 for readability in this instance]
(https://imgur.com/JY0CJt3)

4. Get the current game state by making a GET request to /games/{game_id} endpoint:

![Screenshot of postman input]
(https://imgur.com/Qtvscv3)

5. This will retrieve the current game state, including the masked word, remaining attempts, and previous guesses.

![screenshot of returned gamestate]
(https://imgur.com/XNdI9B6)

6. You can also delete a game by making a DELETE request to /games/{game_id} endpoint:

![screenshot of delete request]
(https://imgur.com/988xJzt)

7. returning the error code of 204:

![screenshot of responded error code]
(https://imgur.com/v1J2nWV)

8. Now when you run /games/{game_id} you will recieve the game status of deleted:

![game has been deleted:]
(https://imgur.com/jDd09H1)

9. So, you must create a new game once again, using a POST request to /games.

10. Now when using a GET response to /games/{game_id} (in this case, 5) we will see that a game is once again in progress. Returning 200.

![/games/5 with game status currently "in progress"]
(https://imgur.com/qirFCql)

11. To guess a letter, modify postman 'headers' with the following edits: 

![Content-Type : application/json, Accept : application/json]
(https://imgur.com/PTEbYrc)

