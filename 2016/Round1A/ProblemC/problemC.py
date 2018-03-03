#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2016
#
# Round 1A - Problem C - BFFs
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def get_chain(i, c_bff, exc):

    max_length = 0

    if i not in c_bff:
        return max_length

    for next_f in c_bff[i]:
        if next_f != exc:
            length = 1 + get_chain(next_f, c_bff, exc)
            max_length = max(length, max_length)

    return max_length


def solve(input_bff):

    d_bff = {i+1: v for i, v in enumerate(input_bff)}
    r_bff = {}
    for i in d_bff:
        v = d_bff[i]
        if v not in r_bff:
            r_bff[v] = [i]
        else:
            r_bff[v].append(i)

    # longest cycle
    longest = 0
    for i in d_bff:
        circle = [i]
        while d_bff[circle[-1]] not in circle:
            circle.append(d_bff[circle[-1]])

        if d_bff[circle[-1]] == circle[0]:
            longest = max(longest, len(circle))

    # longest chains for cycles of lenght two
    sum_chains = 0
    for i in d_bff:
        j = d_bff[i]
        if d_bff[j] == i and j > i:
            sum_chains += get_chain(i, r_bff, j) + get_chain(j, r_bff, i) + 2

    longest = max(longest, sum_chains)

    return longest


input_path = sys.argv[1]

with open(input_path) as input_file:

    n_cases = int(input_file.readline().strip())

    for case in range(1, n_cases+1):
        N = int(input_file.readline().strip())
        bff = map(int, input_file.readline().strip().split())
        solution = solve(bff)
        print('Case #{0}: {1}'.format(case, solution))
