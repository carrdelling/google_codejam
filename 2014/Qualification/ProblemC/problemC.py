#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2014
#
# Qualification round - Problem C - Minesweeper Master
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(rows, columns, mines):

    if rows > columns:
        transpose = True
        r, c = columns, rows
    else:
        transpose = False
        r, c = rows, columns

    free = (r * c) - m

    board = []

    if free == 1:

        for _ in range(r):
            board.append(['*'] * c)

    elif r == 1:
        row = (['.'] * (c - mines)) + (['*'] * mines)
        board.append(row)

    elif r == 2:
        if free > 2 and free % 2 == 0:
            empty = int(free / 2)
            filled = c - empty
            board.append((['.'] * empty) + (['*'] * filled))
            board.append((['.'] * empty) + (['*'] * filled))
    elif free not in {2, 3, 5, 7}:

        # search for two a*2 and b*2 sections (horizontal & vertical rectangles)
        # to place the mines
        a, b = -1, -1
        for _a in range(2, r + 1):
            for _b in range(2, c + 1):
                if 2 * (_a + _b - 2) <= free <= _a * _b:
                    a, b = _a, _b
                    break
            if a > 0:
                break

        # fill the board, clean the first rectangle (a)
        for i in range(r):
            row = ['*'] * c
            if i < a:
                row[0] = '.'
                row[1] = '.'
            board.append(row)

        # clean the second rectangle (b)
        for i in range(c):
            if i < b:
                board[0][i] = '.'
                board[1][i] = '.'

        # clean more mines if necessary - row by row, column by column
        to_clean = free - (2 * (a + b - 2))
        for i in range(2, a):
            for j in range(2, b):
                if to_clean == 0:
                    break
                board[i][j] = '.'
                to_clean -= 1

    if board:
        board[0][0] = 'c'
        if transpose:
            board = list(map(list, zip(*board)))

        return '\n'.join(''.join(row) for row in board)

    return 'Impossible'


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            r, c, m = map(int, input_file.readline().strip().split())
            solution = solve(r, c, m)
            print('Case #{}:'.format(case))
            print(solution)
