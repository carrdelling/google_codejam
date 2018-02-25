#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2014
#
# Qualification round - Problem D - Deceitful War
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(naomi, ken):

    current_naomi = sorted(naomi)
    current_ken = sorted(ken)

    # war
    points = 0
    while current_naomi:
        n = current_naomi.pop()

        for idx, s in enumerate(current_ken):
            if s > n:
                k = s
                current_ken = current_ken[:idx] + current_ken[idx+1:]
                break
        else:
            k = current_ken[0]
            current_ken = current_ken[1:]

        if n > k:
            points += 1

    # deceitful war
    d_points = 0

    current_naomi = sorted(naomi)
    current_ken = sorted(ken)

    while current_naomi:

        while current_naomi and max(current_naomi) < max(current_ken):
            current_naomi.pop(0)
            current_ken.pop()
        else:
            if not current_naomi:
                break

        current_naomi.pop()
        current_ken.pop()
        d_points += 1

    return '{} {}'.format(d_points, points)


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            _ = int(input_file.readline().strip())
            naomi_blocks = list(map(float, input_file.readline().strip().split()))
            ken_blocks = list(map(float, input_file.readline().strip().split()))
            solution = solve(naomi_blocks, ken_blocks)
            print('Case #{}: {}'.format(case, solution))
