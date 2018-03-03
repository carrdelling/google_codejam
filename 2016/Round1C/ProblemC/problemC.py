#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2016
#
# Round 1C - Problem C - Fashion Police
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(j, p, s, k):

    outfits = []

    for _j in range(j):
        for _p in range(p):
            for _k in range(min(k, s)):
                _s = (_j + _p + _k) % s

                outfits.append((_j+1, _p+1, _s+1))

    output = [str(len(outfits))]
    for outfit in outfits:
        output.append(' '.join(map(str, outfit)))

    return '\n'.join(output)


input_path = sys.argv[1]

with open(input_path) as input_file:

    n_cases = int(input_file.readline().strip())

    for case in range(1, n_cases+1):
        j, p, s, k = map(int, input_file.readline().strip().split())
        solution = solve(j, p, s, k)
        print('Case #{0}: {1}'.format(case, solution))
