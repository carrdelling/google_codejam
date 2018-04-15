#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2015
#
# Round1A - Problem A - Mushroom Monster
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(remaining):

    current = remaining[0]
    all_speed = 0
    max_rate = 0

    for size in remaining[1:]:

        if size > current:
            current = size
        else:
            change = current - size
            current = size

            all_speed += change
            max_rate = max(max_rate, change)

    constant_rate = sum(min(max_rate, i) for i in remaining[:-1])

    return '{} {}'.format(all_speed, constant_rate)


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:

        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            N = int(input_file.readline().strip())
            intervals = list(map(int, input_file.readline().strip().split()))
            solution = solve(intervals)
            print('Case #{}: {}'.format(case, solution))
