#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2013
#
# Qualification round - Problem A - Tic-Tac-Toe-Tomek
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys

oo = 'O'
tt = 'T'
xx = 'X'
dot = '.'


def solve(board):

    is_draw = True

    # test rows
    for row in board:
        if dot not in row:
            if oo not in row:
                return 'X won'
            if xx not in row:
                return 'O won'
        else:
            is_draw = False

    # transpose board
    transpose = [list(x) for x in zip(*board)]

    # test columns
    for row in transpose:
        if dot not in row:
            if oo not in row:
                return 'X won'
            if xx not in row:
                return 'O won'

    # test first diag
    n_x = 0
    n_o = 0
    for i in range(4):
        if board[i][i] == dot:
            n_x = 0
            n_o = 0
            break
        if board[i][i] == xx:
            n_x += 1
        if board[i][i] == oo:
            n_o += 1

    if n_o and not n_x:
        return 'O won'
    if n_x and not n_o:
        return 'X won'

    # test second diag
    n_x = 0
    n_o = 0
    for i in range(4):
        if board[i][3-i] == dot:
            n_x = 0
            n_o = 0
            break
        if board[i][3-i] == xx:
            n_x += 1
        if board[i][3-i] == oo:
            n_o += 1

    if n_o and not n_x:
        return 'O won'
    if n_x and not n_o:
        return 'X won'

    if is_draw:
        return 'Draw'
    return 'Game has not completed'

input_path = sys.argv[1]

with open(input_path, 'r') as input_file:

    n_cases = int(input_file.readline().strip())

    for case in range(1, n_cases+1):
        main_board = []
        main_board.append(list(input_file.readline().strip()))
        main_board.append(list(input_file.readline().strip()))
        main_board.append(list(input_file.readline().strip()))
        main_board.append(list(input_file.readline().strip()))
        input_file.readline()
        solution = solve(main_board)
        print('Case #{0}: {1}'.format(case, solution))
