#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2015
#
# Qualification round - Problem B - Infinite House of Pancakes
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys
from collections import Counter


def split_time(size, new_size):

    return (size - 1) / new_size


def solve(s):

    counts = Counter(s)
    largest = max(counts)
    best_time = largest

    for i in range(largest-1, 0, -1):

        split_cost = sum(v * split_time(k, i) for k, v in counts.items())

        cost = i + split_cost

        best_time = min(cost, best_time)

    return best_time


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            _ = input_file.readline().strip()
            sizes = list(map(int, input_file.readline().strip().split()))
            solution = solve(sizes)
            print('Case #{}: {}'.format(case, solution))
