#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2016
#
# Round 1 - Problem B - Rank and File
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(old_parts):

    candidates = set()
    for part in old_parts:
        for c in part:
            if c in candidates:
                candidates.remove(c)
            else:
                candidates.add(c)

    output = sorted(map(int, candidates))

    return ' '.join(map(str, output))

input_path = sys.argv[1]


with open(input_path) as input_file:

    n_cases = int(input_file.readline().strip())

    for case in range(1, n_cases+1):
        N = int(input_file.readline().strip())
        rows = [input_file.readline().strip().split()
                for i in range(0, (2*N)-1)]
        solution = solve(rows)
        print('Case #{0}: {1}'.format(case, solution))
