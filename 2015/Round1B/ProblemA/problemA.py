#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2015
#
# Round1B - Problem A - Counter Culture
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################


import sys


def solve(target):

    if target < 21:
        return target

    steps = 1
    digits = len(str(target))
    left, right = str(target)[:digits//2], str(target)[digits//2:]

    # special case where half of the number are zeroes
    if int(right) == 0:
        return solve(target - 1) + 1

    # 1: count to 1eX, where X=digits
    for d in range(digits):
        # first half
        steps += (10 ** ((d+1) // 2)) - 1

        # flip
        steps += 1 if d > 1 else 0

        # second half
        steps += (10 ** (d // 2)) - 1

    # 2: Count to target

    # if left 100..00, then we can only move forward
    if left == '1' or (left[0] == '1' and int(left[1:]) == 0):
        return steps + int(right)

    # count to the reverse of left
    steps += int(left[::-1])

    # flip
    steps += 1

    # count the rest
    steps += int(right) - 1

    return steps


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            target = int(input_file.readline().strip())
            solution = solve(target)
            print('Case #{}: {}'.format(case, solution))
