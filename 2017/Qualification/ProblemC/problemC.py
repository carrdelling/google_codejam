#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2017
#
# Qualification round - Problem C - Bathroom Stalls
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys
import functools
from collections import Counter


@functools.lru_cache(maxsize=1000)
def split(value):

    n = value >> 1

    return (n, n-1) if value % 2 == 0 else (n, n)


def solve(n, k):

    if n == k:
        return 0, 0

    counter = Counter()
    counter[n] += 1

    left, right = 0, 0
    while k > 0:
        current = max(counter)

        if counter[current] <= k:
            tries = counter[current]
            left, right = split(current)
            k -= tries
            counter.pop(current)
            counter[left] += tries
            counter[right] += tries

        else:
            tries = k
            left, right = split(current)
            k -= tries
            counter[current] -= tries
            counter[left] += tries
            counter[right] += tries

    return left, right


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:

        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            stalls, users = map(int, input_file.readline().strip().split())
            solution = solve(stalls, users)
            print('Case #{0}: {1} {2}'.format(case, solution[0], solution[1]))
