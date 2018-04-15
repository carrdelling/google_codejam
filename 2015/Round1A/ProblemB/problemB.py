#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2015
#
# Round1A - Problem B - Haircut
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def served_at(barbers, times, t):

    # how many people were served at time t?

    served = 0

    for i in range(barbers):

        served += t // times[i]

        if t % times[i] != 0:
            served += 1

    return served


def solve(barbers, target, times):

    # get as close to the target as possible
    min_t = 0
    max_t = 1E18
    while min_t < max_t:
        t = (min_t + max_t) // 2
        if served_at(barbers, times, t) < target:
            min_t = t + 1
        else:
            max_t = t
    t = min_t - 1

    # check the last iteration
    already_served = served_at(barbers, times, t)
    for i in range(barbers):
        if t % times[i] == 0:
            already_served += 1
            if already_served == target:
                return i + 1


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:

        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            B, N = map(int, input_file.readline().strip().split())
            M = list(map(int, input_file.readline().strip().split()))
            solution = solve(B, N, M)
            print('Case #{}: {}'.format(case, solution))
