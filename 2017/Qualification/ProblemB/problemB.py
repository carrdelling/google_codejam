#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2017
#
# Qualification round - Problem B - Tidy Numbers
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(N):

    number = list(map(int, N))
    put_nines = False
    for i in range(1, len(number)):

        if put_nines:
            number[i] = 9
            continue

        if number[i-1] > number[i]:

            # fix forward
            number[i] = 9
            put_nines = True

            # fix backwards
            number[i-1] -= 1
            for j in range(i-2, -1, -1):
                if number[j] > number[j+1]:
                    number[j+1] = 9
                    number[j] -= 1

    return int(''.join(map(str, number)))

if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:

        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            N = input_file.readline().strip()
            solution = solve(N)
            print('Case #{0}: {1}'.format(case, solution))
