#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2017
#
# Qualification round - Problem D - Fashion Show
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys
from itertools import product
from collections import defaultdict

EMPTY = 0
CROSS = 1
XX = 2
CIRCLE = 3

scores = {CROSS: 1,
          XX: 1,
          CIRCLE: 2,
          EMPTY: 0}


def solve(N, board):

    new_models = defaultdict(list)

    # x - blocked
    x_blocked_x = set()
    x_blocked_y = set()

    for i, j in product(range(N), range(N)):
        if board[i][j] in {XX, CIRCLE}:
            x_blocked_x.add(i)
            x_blocked_y.add(j)

    # + - blocked
    cross_blocked_x = set()
    cross_blocked_y = set()
    for i, j in product(range(N), range(N)):
        if board[i][j] in {CROSS, CIRCLE}:
            cross_blocked_x.add(i + j)
            cross_blocked_y.add(i - j)

    # add x
    for i, j in product(range(N), range(N)):
        if i not in x_blocked_x and j not in x_blocked_y:
            if board[i][j] == CROSS:
                new_models[CIRCLE].append((i, j))
                board[i][j] = CIRCLE
            else:
                new_models[XX].append((i, j))
                board[i][j] = XX
            x_blocked_x.add(i)
            x_blocked_y.add(j)

    # add +

    # this is the tricky part (too tricky for a qualification problem, maybe): the order
    # for checking the + should be following the diagonals from both the upper left
    # side (going down-left) and the lower-right side (going up-right) of the board
    o2 = []
    for i in range(N - 1):  # keep i+j constant
        for j in range(i + 1):
            o2.append((j, i - j))  # upper-left diagonal
            o2.append((N - 1 - j, N - 1 - i + j))   # lower-right diagonal
    # finally, add the mid diagonal
    for j in range(N):
        value = (j, N - 1 - j)
        o2.append(value)

    for i, j in o2:
        if i + j not in cross_blocked_x and i - j not in cross_blocked_y:
            if board[i][j] == XX:
                new_models[CIRCLE].append((i, j))
                board[i][j] = CIRCLE
                if (i, j) in new_models[XX]:
                    new_models[XX].remove((i, j))
            else:
                new_models[CROSS].append((i, j))
                board[i][j] = CROSS
            cross_blocked_x.add(i + j)
            cross_blocked_y.add(i - j)

    n_new = len(new_models[CROSS] + new_models[XX] + new_models[CIRCLE])
    score = sum(scores[board[i][j]] for i, j in product(range(N), range(N)))

    output = ['{} {}'.format(score, n_new)]

    for i, j in new_models[CROSS]:
        output.append('+ {} {}'.format(i+1, j+1))

    for i, j in new_models[XX]:
        output.append('x {} {}'.format(i+1, j+1))

    for i, j in new_models[CIRCLE]:
        output.append('o {} {}'.format(i+1, j+1))

    return '\n'.join(output)


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:

        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            N, M = map(int, input_file.readline().strip().split())

            models = []
            if M > 0:
                for _ in range(M):
                    typ, r, c = input_file.readline().strip().split()
                    models.append((typ, int(r), int(c)))
            board = []
            for _ in range(N):
                board.append([EMPTY] * N)

            for t, r, c in models:

                if t == '+':
                    v = CROSS
                elif t == 'x':
                    v = XX
                else:
                    v = CIRCLE

                board[r-1][c-1] = v

            solution = solve(N, board)
            print('Case #{0}: {1}'.format(case, solution))
