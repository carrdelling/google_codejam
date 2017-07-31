#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2011
#
# Qualification round - Problem A - Bot Trust
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(tasks):

    time = 0

    pos_o = 1
    pos_b = 1
    turns_o = 0
    turns_b = 0

    for task in tasks:

        bot, number = task

        if bot == 'B':
            cost = abs(pos_b-number) + 1
            real_cost = max(cost-turns_b, 1)
            turns_b = 0
            pos_b = number
            turns_o += real_cost
            time += real_cost

        if bot == 'O':
            cost = abs(pos_o-number) + 1
            real_cost = max(cost-turns_o, 1)
            turns_o = 0
            pos_o = number
            turns_b += real_cost
            time += real_cost

    return time


input_path = sys.argv[1]

with open(input_path, 'r') as input_file:

    n_cases = int(input_file.readline().strip())

    for case in range(1, n_cases+1):

        sequence = input_file.readline().strip().split()[1:]
        sequence = zip(sequence[:-1], sequence[1:])[::2]
        sequence = [(x, int(y)) for (x, y) in sequence]

        solution = solve(sequence)
        print('Case #{0}: {1}'.format(case, solution))
