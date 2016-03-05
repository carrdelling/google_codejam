#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2012
#
# Qualification round - Problem C - Recycled Numbers
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def seek_pair(n, a, b):

    initial = str(n)

    for i in xrange(1, len(initial)):

        current = int(initial[-i:] + initial[:-i])

        if (a <= current <= b) and n != current:
            yield current


def solve(down, up):

    pairs = set()

    down = max(down, 12)

    for number in xrange(down, up+1):

        for pair in seek_pair(number, down, up):
            option = (min(pair, number), max(pair, number))
            pairs.add(option)

    return len(pairs)


input_path = sys.argv[1]

with open(input_path, 'r') as input_file:

    n_cases = int(input_file.readline().strip())

    for case in xrange(1, n_cases+1):
        A, B = map(int, input_file.readline().strip().split())
        solution = solve(A, B)

        print 'Case #{0}: {1}'.format(case, solution)
