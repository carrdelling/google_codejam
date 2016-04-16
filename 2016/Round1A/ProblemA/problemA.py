#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2016
#
# Round 1 - Problem A - The Last Word
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(word):

    output = word[0]

    for c in word[1:]:
        if c >= output[0]:
            output = c + output
        else:
            output += c

    return output


input_path = sys.argv[1]

with open(input_path) as input_file:

    n_cases = int(input_file.readline().strip())

    for case in xrange(1, n_cases+1):
        input_word = input_file.readline().strip().split()
        solution = solve(input_word[0])
        print 'Case #{0}: {1}'.format(case, solution)
