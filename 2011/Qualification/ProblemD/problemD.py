#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2011
#
# Qualification round - Problem D - GoroSort
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(array):

    return sum([1 for index, value in enumerate(array) if index+1 != value])

input_path = sys.argv[1]

with open(input_path, 'r') as input_file:

    n_cases = int(input_file.readline().strip())

    for case in range(1, n_cases+1):

        N = int(input_file.readline().strip())
        array = map(int, input_file.readline().strip().split())

        solution = solve(array)

        print('Case #{0}: {1}'.format(case, solution))
