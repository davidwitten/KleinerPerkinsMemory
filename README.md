# Kleiner Perkins Memory Game
## Rules
1. Mix up the cards.

2. Lay them in rows of 4 face down.

3. Each player takes turns turning over any two cards.

4. If the two cards match, take them.

5. If they don't match, turn them back over and move to the next person.

6. The game is over when all the cards have been matched.

7. The player with the most cards matched wins.

## Design decisions
In terms of data structures, I made a decision to store the cards in a single-dimension array and store the players' information as an array of integers. I chose to 

In terms of code organization, I made a decision to create a class for the game and a class for an individual card. This helps in a few ways. First, it makes it much easier to stay organized. I can create a game just by doing:

`game = Memory(# of players)`

Additionally, I overloaded some operators, so `print(game)` prints the board. Additionally, comparing two cards is just `card1 == card2`. This improves readability and makes it easier to write.

## Language choice

I chose to code this in Python, because it is easier to read and more concise. This is a simple game, so I didn't choose C++ for the performance improvements.
