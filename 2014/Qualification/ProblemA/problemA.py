#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2014
#
# Qualification round - Problem A - Magic Trick
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(board1, board2, row1, row2):

    possibilities = set(board1[row1 - 1]) & set(board2[row2 - 1])

    if len(possibilities) > 1:
        return "Bad magician!"
    elif len(possibilities) == 1:
        return next(iter(possibilities))
    else:
        return "Volunteer cheated!"


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            first_answer = int(input_file.readline().strip())
            first_board = []
            for i in range(4):
                cards = list(map(int, input_file.readline().strip().split()))
                first_board.append(cards)
            second_answer = int(input_file.readline().strip())
            second_board = []
            for i in range(4):
                cards = list(map(int, input_file.readline().strip().split()))
                second_board.append(cards)
            solution = solve(first_board, second_board, first_answer, second_answer)
            print('Case #{}: {}'.format(case, solution))
