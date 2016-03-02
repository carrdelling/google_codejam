#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2011
#
# Qualification round - Problem C - Candy Splitting
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(candy_bag):

    candy_bag.sort()
    all_sum = sum(candy_bag)

    all = reduce(lambda x, y: x ^ y, candy_bag)

    for candy in candy_bag:
        rest = all ^ candy
        if not rest ^ candy:
            return all_sum - candy

    return 'NO'

input_path = sys.argv[1]

with open(input_path, 'r') as input_file:

    n_cases = int(input_file.readline().strip())

    for case in xrange(1, n_cases+1):

        N = int(input_file.readline().strip())
        candy = map(int, input_file.readline().strip().split())

        solution = solve(candy)

        print 'Case #{0}: {1}'.format(case, solution)
