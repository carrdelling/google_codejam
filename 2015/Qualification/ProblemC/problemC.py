#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2015
#
# Qualification round - Problem C - Dijkstra
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys

transl_d = {('z', 'z'): 'z',
            ('z', 'i'): 'i',
            ('z', 'j'): 'j',
            ('z', 'k'): 'k',
            ('z', 'Z'): 'Z',
            ('z', 'I'): 'I',
            ('z', 'J'): 'J',
            ('z', 'K'): 'K',
            ('Z', 'z'): 'Z',
            ('Z', 'i'): 'I',
            ('Z', 'j'): 'J',
            ('Z', 'k'): 'K',
            ('Z', 'Z'): 'z',
            ('Z', 'I'): 'i',
            ('Z', 'J'): 'j',
            ('Z', 'K'): 'k',
            ('i', 'z'): 'i',
            ('i', 'i'): 'Z',
            ('i', 'j'): 'k',
            ('i', 'k'): 'J',
            ('i', 'Z'): 'I',
            ('i', 'I'): 'z',
            ('i', 'J'): 'K',
            ('i', 'K'): 'j',
            ('I', 'z'): 'I',
            ('I', 'i'): 'z',
            ('I', 'j'): 'K',
            ('I', 'k'): 'j',
            ('I', 'Z'): 'i',
            ('I', 'I'): 'Z',
            ('I', 'J'): 'k',
            ('I', 'K'): 'J',
            ('j', 'z'): 'j',
            ('j', 'i'): 'K',
            ('j', 'j'): 'Z',
            ('j', 'k'): 'i',
            ('j', 'Z'): 'J',
            ('j', 'I'): 'k',
            ('j', 'J'): 'z',
            ('j', 'K'): 'I',
            ('J', 'z'): 'J',
            ('J', 'i'): 'k',
            ('J', 'j'): 'z',
            ('J', 'k'): 'I',
            ('J', 'Z'): 'j',
            ('J', 'I'): 'K',
            ('J', 'J'): 'Z',
            ('J', 'K'): 'i',
            ('k', 'z'): 'k',
            ('k', 'i'): 'j',
            ('k', 'j'): 'I',
            ('k', 'k'): 'Z',
            ('k', 'Z'): 'K',
            ('k', 'I'): 'J',
            ('k', 'J'): 'i',
            ('k', 'K'): 'z',
            ('K', 'z'): 'K',
            ('K', 'i'): 'J',
            ('K', 'j'): 'i',
            ('K', 'k'): 'z',
            ('K', 'Z'): 'k',
            ('K', 'I'): 'j',
            ('K', 'J'): 'I',
            ('K', 'K'): 'Z'}

TOO_MANY_TRIES = 20


def reduce_problem(problem):

    while len(problem) > 1:
        problem = transl_d[(problem[0], problem[1])] + problem[2:]

    return problem


def solve(string, r):

    if len(string) < 2:
        return 'NO'

    # find if a 'i' is possible at the beginning of the string
    left = string
    current_r = r - 1

    while left[0] != 'i':

        # expand if necessary
        if len(left) < 2:
            if current_r < 1:
                return 'NO'
            else:
                left = left + string
                current_r -= 1

                # stop the search if we have tried too many times
                if (r - current_r) > TOO_MANY_TRIES:
                    return 'NO'

        left = transl_d[(left[0], left[1])] + left[2:]

    # we have found an 'i' -- update left and take it out
    left = left[1:]

    # find if a 'k' is possible at the end of the string
    if current_r < 1:
        right = left
        left = ''
    else:
        right = string

    current_r -= 1

    while right[-1] != 'k':

        # expand if necessary
        if len(right) < 2:
            if current_r < 0:
                return 'NO'
            else:
                if current_r == 0:
                    if len(left) < 1:
                        return 'NO'
                    right = left + right
                    current_r -= 1
                    left = ''

                else:
                    right = string + right
                    current_r -= 1

                # stop the search if we have tried too many times
                if (r - current_r) > TOO_MANY_TRIES:
                    return 'NO'

        right = right[:-2] + transl_d[(right[-2], right[-1])]

    # we have found a 'k' -- update right and take it out
    right = right[:-1]

    # consolidate the rest of the string
    if current_r > 0:
        new_problem = reduce_problem(string)

        # consolidate problem
        repeats = current_r % 4
        new_problem = new_problem * repeats if repeats else 'z'

        center = left + new_problem + right
    elif current_r == 0:
        center = left + right
    else:
        center = right

    # try to find 'j' in center
    center = reduce_problem(center)

    return 'YES' if center == 'j' else 'NO'


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            _, repeat = map(int, input_file.readline().strip().split())
            pattern = input_file.readline().strip()

            solution = solve(pattern, repeat)
            print('Case #{}: {}'.format(case, solution))
