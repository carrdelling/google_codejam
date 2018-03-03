#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2016
#
# Round 1A - Problem A - Getting the Digits
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################


import sys
from collections import Counter

"""
some rules

Z ---> 0
W ---> 2
X ---> 6 
G ---> 8
T ---> 3
U ---> 4
S ---> 7
O ---> 1
V ---> 5
I / 2 --> 9

"""


def find_number(key, name, counts):

    times = counts.get(key, 0)
    for char in name:
        counts[char] = max(0, counts.get(char, 0) - times)

    return times


def solve(string):

    counts = Counter(string)
    solution = []

    rules = [('Z', "ZERO", '0'),
             ('W', "TWO", '2'),
             ('X', "SIX", '6'),
             ('G', "EIGHT", '8'),
             ('T', "THREE", '3'),
             ('U', "FOUR", '4'),
             ('S', "SEVEN", '7'),
             ('O', "ONE", '1'),
             ('V', "FIVE", '5'),
             ('I', "NINE", '9')
             ]

    for rule in rules:
        times = find_number(rule[0], rule[1], counts)
        solution += rule[2] * times

    return ''.join(sorted(solution))


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())
        for case in range(1, n_cases+1):
            s = input_file.readline().strip()
            solution = solve(s)
            print('Case #{}: {}'.format(case, solution))
