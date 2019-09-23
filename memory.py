import os
from random import shuffle

"""
    Clears the terminal to make it easier to read
    Also ensure that players can't easily see past moves
"""
def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Card:
    """
        Each card stores three values:
        The number (value)
        The suit (suit)
        What is displayed to the players (display)
    """

    def __init__(self, value, suit, display):
        self.value = value
        self.suit = suit
        self.display = display

    """
        Given a list of [value, suit, output], return the card
        e.g. [0,0,1] -> 2 of Spades
    """
    def __str__(self):
        suit = ['Spades', 'Clubs', 'Hearts', 'Diamonds'][self.suit]
        num = str(self.value + 2)
        if self.value >= 9:
            num = ['Jack', 'Queen', 'King', 'Ace'][self.value - 9]
        return num + " of " + suit

    """
        Turns the card over, revealing the card's value to the player
    """
    def reveal(self):
        self.display = str(self)

    """
        Checks if this card is equal to another card (according to this game's rules)
    """
    def __eq__(self, other):
        return self.value == other.value

class Memory:

    """
        Initializes a playing board, and a list of player scores
    """
    def __init__(self, players):
        # Randomized deck
        deck = list(range(52))
        shuffle(deck)

        # Board. Each element includes the number, suit, and what is outputted
        self.board = [Card(el % 13, el // 13, ind + 1) for ind, el in enumerate(deck)]

        # List of the scores for each person
        self.players = [0 for i in range(players)]

    """
        Overloads the print(...) operator
        This way, it's very easy to print
        Build the list as fast as possible, by doing ''.join(array)
        This is faster than doing string concatenation, which is O(n**2)
        to build the entire string
    """
    def __repr__(self):
        full_out = []
        for row in range(13):
            out = []
            for col in range(4):
                loc = self.board[4 * row + col].display
                # Left justifies the print in a window of 18 characters
                # 17 characters is the longest name: "Queen of Diamonds"
                out.append('{:17}'.format(str(loc)))
            full_out.append("".join(out))
        return "\n".join(full_out)

    """
        One player's round:
        Turn over one card, turn over a second
        If they're equal, you win 2 points. Otherwise, turn them back over
    """
    def show(self, player):
        choices = [0, 0]
        for i in range(2):
            # Choose the first card and ensure that it's valid
            valid_input = False
            while not valid_input:
                choices[i] = input("Pick a card!")
                valid_input = self.valid_input(choices[i])

            # Flip the card over
            clearscreen()
            self.board[int(choices[i]) - 1].reveal()
            print(self)

        # The two cards match:
        if self.board[int(choices[0]) - 1] == self.board[int(choices[1]) - 1]:
            self.players[player] += 2
            print("Nice! Here are the scores now:")
            self.results()

            # Removes the cards from the pile. You can no longer see them
            self.board[int(choices[0]) - 1].display = ""
            self.board[int(choices[1]) - 1].display = ""
        else:
            print("Sorry, nice try!")
            self.board[int(choices[0]) - 1].display = int(choices[0])
            self.board[int(choices[1]) - 1].display = int(choices[1])

        input("Press any key to continue.")
        clearscreen()

    """
        Helper function: determine if an input is valid
        If it's not an integer or outside of 1-52, it's invalid
        If it's already been picked, it's invalid
    """
    def valid_input(self, position):
        if not position.isnumeric() or not 1 <= int(position) <= 52:
            print("Please input a number from 1-52.")
            return False
        if self.board[int(position) - 1].display != int(position):
            print("This has already been picked. Pick again")
            return False
        # Valid input
        return True

    """
        Return if the board is empty
    """
    def is_empty(self):
        return 52 - sum(self.players) == 0

    """
        Helper function: output the results
    """
    def results(self):
        for player, score in enumerate(self.players, 1):
            print("Player {}: {} points".format(player, score))


def main():
    print("Welcome to Memory! The object of this game is to pick two cards with the same number")
    number_of_players = int(input("How many players do you want?"))
    input("Press any key when you're ready to start!")
    game = Memory(number_of_players)
    while not game.is_empty():
        for i in range(number_of_players):
            print(game)
            print("Ready player " + str(i + 1) + "?")
            game.show(i)
            if game.is_empty():
                print("Congrats player {i}!!".format(i + 1))
                print("Here are the final standings:")
                game.results()
                break

if __name__ == "__main__":
    main()
