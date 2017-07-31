#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2012
#
# Qualification round - Problem B - Dancing with the Googlers
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(s, p, scores):

    winners = 0

    for goog in scores:

        if p == 0:
            winners += 1
            continue

        if p == 1:
            winners += 1 if goog > 0 else 0
            continue

        # unsurprising minimum score
        unsurprising = ((p - 1) * 3) + 1

        if goog >= unsurprising:
            winners += 1
            continue

        # surprising ?
        if s > 0 and goog >= unsurprising - 2:
            s -= 1
            winners += 1

    return winners


input_path = sys.argv[1]

with open(input_path, 'r') as input_file:

    n_cases = int(input_file.readline().strip())

    for case in range(1, n_cases+1):

        sequence = map(int, input_file.readline().strip().split())
        _, _S, _P = sequence[:3]
        _scores = sequence[3:]
        solution = solve(_S, _P, _scores)

        print('Case #{0}: {1}'.format(case, solution))
