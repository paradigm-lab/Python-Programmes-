import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter


    # We want all players to get their next move given a game
    def get_move(self, game):
        pass

# We are using inheritance to create the randomComputerPlayer
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square



class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "\'s turn. Input move(0-9):")

            # We are going to check that this is  correct value by trying to cast
            # It to an integer, and if it is not, then we say its invalid
            # if that spot is not available on the board, we also say its invalid.
        
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True     # if these are succcessful, Then yay!
            except ValueError:
                print("Invalid square. Try again.")

        return val
            

