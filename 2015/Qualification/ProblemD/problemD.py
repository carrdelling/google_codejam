#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2015
#
# Qualification round - Problem D - Ominous Omino
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(x, r, c):

    if x == 1:
        return "GABRIEL"

    # if x => 7, Richard can pick a block with a hole -> so he wins always
    if x >= 7:
        return "RICHARD"

    # check the modulo condition (Richard can pick a block that does not fit)
    if r * c % x != 0:
        return "RICHARD"

    if x == 2:
        return "GABRIEL"
    if x == 3:
        if r == 1 or c == 1:
            return "RICHARD"
        return "GABRIEL"

    if x == 4:
        if min(r, c) > 2:
            return "GABRIEL"
        return "RICHARD"

    if x == 5:
        if min(r, c) > 2 and (r, c) not in {(3, 5), (5, 3)}:
            return "GABRIEL"
        return "RICHARD"

    # if X == 6
    if r <= 3 or c <= 3:
        return "RICHARD"

    return "GABRIEL"


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())
        for case in range(1, n_cases+1):
            level, rows, columns = map(int, input_file.readline().strip().split())
            solution = solve(level, rows, columns)
            print('Case #{}: {}'.format(case, solution))
