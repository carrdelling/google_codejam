#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2013
#
# Qualification round - Problem B - Lawnmower
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys

oo = 'O'
tt = 'T'
xx = 'X'
dot = '.'


def solve(n, m, board):

    field = [[100] * m] * n

    # cut rows
    for i in range(n):
        h = max(board[i])
        field[i] = [h] * m

    # cut columns
    transpose_field = [list(x) for x in zip(*field)]
    transpose_board = [list(x) for x in zip(*board)]

    for i in range(m):
        h = max(transpose_board[i])
        for j in range(n):
            transpose_field[i][j] = min(transpose_field[i][j], h)

    # compare output
    final_field = [list(x) for x in zip(*transpose_field)]

    for i in range(n):
        for j in range(m):
            if final_field[i][j] != board[i][j]:
                return 'NO'

    return 'YES'

input_path = sys.argv[1]

with open(input_path, 'r') as input_file:

    n_cases = int(input_file.readline().strip())

    for case in range(1, n_cases+1):
        N, M = map(int, input_file.readline().strip().split())
        board = []
        for i in range(N):
            row = map(int, input_file.readline().strip().split())
            board.append(row)
        solution = solve(N, M, board)
        print('Case #{0}: {1}'.format(case, solution))
