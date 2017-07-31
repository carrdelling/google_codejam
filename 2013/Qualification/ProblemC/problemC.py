#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2013
#
# Qualification round - Problem C - Fair and Square
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys
import logging as lgg


def check(s, pattern, fair_square):

    reverse = s[::-1]

    prefix = s if pattern & 1 == 0 else s[:-1]
    aux = int(prefix + reverse)
    s2 = str(aux*aux)

    if s2 == s2[::-1]:
        fair_square.append(s2)


def step(s, limit, test_two, pattern, fair_square):

    if limit == 0:
        check(s, pattern, fair_square)
    else:
        limit -= 1
        step(s+'0', limit, test_two, pattern, fair_square)
        step(s+'1', limit, test_two, pattern, fair_square)
        if test_two > 0:
            step(s+'2', limit, test_two-1, pattern, fair_square)


def precompute():

    lgg.basicConfig(level=lgg.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

    fair_square = [1, 4, 9]

    limit = 51

    for length in range(2, limit):
        half = length - (length >> 1)
        step('1', half-1, 1, length, fair_square)
        step('2', half-1, 0, length, fair_square)
        lgg.info('L = {0}'.format(length))

    with open('fair_square_numbers', 'w') as output_file:

        output_file.write('\n'.join(map(str, fair_square)))


def solve(a, b, numbers):

    output = sum([1 for n in numbers if a <= n <= b])

    return output


def load_numbers():

    output = set()

    with open('fair_square_numbers') as input_numbers:
        for row in input_numbers:
            output.add(int(row.strip()))

    return output

# about 33 mins - single core
# precompute()
numbers = load_numbers()

input_path = sys.argv[1]

with open(input_path, 'r') as input_file:

    n_cases = int(input_file.readline().strip())

    for case in range(1, n_cases+1):
        a, b = map(int, input_file.readline().strip().split())
        solution = solve(a, b, numbers)
        print('Case #{0}: {1}'.format(case, solution))
