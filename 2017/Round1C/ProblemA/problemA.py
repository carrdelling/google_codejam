#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2017
#
# Round 1C - Problem A - Ample Syrup
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys
from math import pi


def area(r):

    return pi * (r ** 2)


def lon(r, h):

    return 2 * pi * h * r


def solve(k, pans):
    """  Solve the problem """

    # compute value (side area) of each and sort
    for p in pans:
        p.append(lon(p[0], p[1]))

    pans.sort(key=lambda x: x[2], reverse=True)

    # selected group
    selected = [list(p) for p in pans[:k]]
    max_r = max(p[0] for p in selected)

    for p in pans[K:]:
        if p[0] > max_r:
            gain_r = area(p[0]) - area(max_r)
            loss_h = selected[-1][2] - p[2]

            if gain_r > loss_h:
                selected[-1] = list(p)
                max_r = p[0]

    # compute final solution
    h_score = sum(p[2] for p in selected)
    area_score = area(max_r)

    return h_score + area_score


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:

        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            N, K = list(map(int, input_file.readline().strip().split()))

            pancakes = []

            for _ in range(N):
                pan = list(map(int, input_file.readline().strip().split()))
                pancakes.append(pan)

            solution = solve(K, pancakes)
            print('Case #{0}: {1}'.format(case, solution))
