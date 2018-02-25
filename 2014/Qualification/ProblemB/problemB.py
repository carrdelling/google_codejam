#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2014
#
# Qualification round - Problem B - Cookie clicker
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(cost, farm, target):

    rate = 2.0
    spent = 0.0

    estimated = target / rate
    improved = (cost / rate) + (target / (rate + farm))

    while estimated > improved:

        spent += (cost/rate)
        rate += farm

        estimated = target / rate
        improved = (cost / rate) + (target / (rate + farm))
    else:
        spent += (target / rate)

    return spent


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            c, f, x = map(float, input_file.readline().strip().split())
            solution = solve(c, f, x)
            print('Case #{}: {}'.format(case, solution))
