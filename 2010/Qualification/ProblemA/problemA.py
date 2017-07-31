#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2010
#
# Qualification round - Problem A - Snapper Chain
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(n, k):

    if k < 1:
        return 'OFF'

    # k in binary repr
    binary = str(bin(k))[2:]

    on = True
    if len(binary) < n:
        on = False
    else:
        mask = binary[-n:]
        for b in mask:
            if b != '1':
                on = False
                break

    return 'ON' if on else 'OFF'

input_path = sys.argv[1]

with open(input_path, 'r') as input_file:

    n_cases = int(input_file.readline().strip())

    for i in range(n_cases):

        n_value, k_value = map(int, input_file.readline().strip().split())

        solution = solve(n_value, k_value)

        print('Case #%d: %s' % (i+1, solution))
