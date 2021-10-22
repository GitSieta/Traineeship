from behave import *
from tictactoe import EMPTY_BOARD, play, play_best_move

@given(u'we have an empty tic-tac-toe board')
def step_impl(context):
    context.board = EMPTY_BOARD
    context.winner = "None"

@when(u'I play X on column {column} and row {row} on the board')
def step_impl(context, column, row):
    context.board, context.winner = play(context.board, "X", (int(column)-1), (int(row)-1))

@when(u'I ask the computer to do its best move for O')
def step_impl(context):
    context.board, context.winner = play_best_move(context.board, "O")

@then(u'the board has a O in column 1 and row 1 on the board')
def step_impl(context):
    context.board[1] == "O"

@then(u'the winner is {winner}')
def step_impl(context, winner):
    if winner == "undecided":
        assert context.winner == "T"
    else:
        assert context.winner == winner