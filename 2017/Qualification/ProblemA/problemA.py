#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2017
#
# Qualification round - Problem A - Oversized Pancake Flipper
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(row, K):

    row = list(map(lambda x: 0 if x == '-' else 1, row))
    N = len(row)

    flips = 0
    for i in range(N-K+1):

        if row[i] % 2 == 0:
            for j in range(i, i+K):
                row[j] += 1
            flips += 1

    for i in range(N-K+1, N):
        if row[i] % 2 == 0:
            return "IMPOSSIBLE"

    return flips

if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:

        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            S, K = input_file.readline().strip().split()
            solution = solve(S, int(K))
            print('Case #{0}: {1}'.format(case, solution))
