# Kleiner Perkins Memory Game
## Rules
For this game, I'm using the standard rules of Memory/Concentration:

1. Mix up the cards.

2. Lay them in rows of 4 face down.

3. Each player takes turns turning over any two cards.

4. If the two cards match, take them.

5. If they don't match, turn them back over and move to the next person.

6. The game is over when all the cards have been matched.

7. The player with the most cards matched wins.

## Instructions

In order to run this code, all you have to do is to navigate to the directory with the  file and enter the following command into the terminal.

`python3 memory.py`

## Design decisions
In terms of data structures, I made a decision to store the cards in a single-dimension array and store the players' information as an array of integers. This makes the game simpler, and allows for us to locate and flip a card in O(1) time. 

In terms of code organization, I made a decision to create a class for the game and a class for an individual card. This helps in a few ways. First, it makes it much easier to stay organized. I can create a game just by doing:

`game = Memory(# of players)`

Additionally, I overloaded some operators, so `print(game)` prints the board. Additionally, comparing two cards is just `card1 == card2`. This improves readability and makes it easier to write. Additionally, the single-dimension array that stored the deck of cards stored Card objects, which include the #, the suit, and what to display to the viewer (the back or front of the card).

I have a few helper methods, including `valid_input`, which checks that the player isn't picking an invalid card (e.g. inputting a decimal or a string) or a card that has already been revealed.

Finally, after every move, I clear the terminal. Therefore, unless the player scrolls up in the terminal, they cannot see past moves. This also ensures that the board is at the top of the terminal every time a player moves, which is more visually appealing. 

## Language choice

I chose to write this in Python, because it is easier to read and more concise. I used as few external libraries as possible. I used thie built-in `os` Python module to clear the terminal screen. I used the built-in `random` module to shuffle the deck of cards.
