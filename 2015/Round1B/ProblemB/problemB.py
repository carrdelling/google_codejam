#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2015
#
# Round1B - Problem B - Noisy Neighbors
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(r, c, n):

    # compute tenants above half the building
    tenants = n - (r * c + 1) // 2
    if tenants < 1:
        return 0

    # with a single row/column, each extra tenant adds 2 of unhapiness
    # if total size is odd, the first tenant only adds 1
    if r == 1 or c == 1:
        if r * c % 2 == 0:
            return (2 * tenants) - 1
        else:
            return 2 * tenants

    # if the building is even sized
    if r * c % 2 == 0:
        u = 0

        # the first two tenants only add 2 (squares)
        u += 2 * min(tenants, 2)
        tenants -= 2

        # the next r + c - 4 tenants only add 3 (borders)
        u += max(3 * min(tenants, r + c - 4), 0)
        tenants -= r + c - 4

        # the rest of the tenants (if any) add 4
        u += max(4 * tenants, 0)
        return u

    # if the building is odd sized, but we only have one extra tenant, the cost is 3
    if tenants == 1:
        return 3

    u = 0

    # since the building is odd size, we need to consider an extra tenant
    tenants += 1

    # the first four tenants only add 2 (squares)
    u += 2 * min(tenants, 4)
    tenants -= 4

    # the next r + c - 6 tenants only add 3 (borders)
    u += max(3 * min(tenants, r + c - 6), 0)
    tenants -= r + c - 6

    # the rest of the tenants (if any) add 4
    u += max(4 * tenants, 0)
    return u


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            row, col, t = map(int, input_file.readline().strip().split())
            solution = solve(row, col, t)
            print('Case #{}: {}'.format(case, solution))
