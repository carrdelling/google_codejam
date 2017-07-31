#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2012
#
# Qualification round - Problem A - Speaking in Tonges
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


mappings = {'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c',
            'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g',
            'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't',
            's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm',
            'y': 'a', 'z': 'q', ' ': ' ', '\n': ''}


def solve(msg):

    output = []
    for char in msg:
        output.append(mappings[char])

    return ''.join(output)


input_path = sys.argv[1]

with open(input_path, 'r') as input_file:

    n_cases = int(input_file.readline().strip())

    for case in range(1, n_cases+1):
        message = input_file.readline()
        solution = solve(message)
        print('Case #{0}: {1}'.format(case, solution))
