class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # We will use a single list to represent 3x3
        self.current_winner = None            # Keep track of winner!


    def print_board(self):
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')


    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (Tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')


    def available_moves(self):
        # Using the list comprehasion 
        # return [i for i, spot in enumarate(self.board) if spot == ' ']

        moves = []
        for (i, spot) in enumarate(self.board):
            # ['x', 'x', 'o'] --> (0, 'x'), (1, 'x'), (2, 'o')]
            if spot == ' ':
                moves.append(i)
        return moves

    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # Then return true. If invalid, Return false
        if self.board[square] = ' ':
            self.board[square] = letter
            return True
        return False


    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return len(self.available_moves())
        '''
            OR
            return self.board.count(' ')
        '''


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    # Iterate while the game still has empty squares
    # (We don't have to worry about winner because we'll just return that
    # which breaks the loop)

    while game.empty_squares():
        # Get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # let's define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" Makes a move to square {square}")
                game.print_board()
                print('') # just empty line

            # After we made our move, We need to alternate letters
            letter = 'O' if letter == 'X' else 'X'





