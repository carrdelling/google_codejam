#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2015
#
# Qualification round - Problem A - Standing Ovation
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(k_string):

    missing = 0
    extra = 0
    for v in k_string:
        _v = int(v)

        extra += _v
        if extra > 0:
            extra -= 1
        else:
            missing += 1

    return missing


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            _, public = input_file.readline().strip().split()
            solution = solve(public)
            print('Case #{}: {}'.format(case, solution))
