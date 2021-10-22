from tictactoe import EMPTY_BOARD, play

board = EMPTY_BOARD # clear the 3 x 3 tictactoe board
winner = None # set the winner to None

board, winner = play(board, 'X', 1, 1) # winner == None
board, winner = play(board, 'O', 0, 0) # winner == None
board, winner = play(board, 'X', 1, 0) # winner == None
board, winner = play(board, 'O', 0, 2) # winner == None
board, winner = play(board, 'X', 1, 2) # winner == X