#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2010
#
# Qualification round - Problem B - Fair Warning
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def gcd(a, b):

    while b > 0:
        r = a % b
        a = b
        b = r

    return a


def solve(events):
    y = events[0]
    distances = [abs(x - y) for x in events]
    g = reduce(gcd, distances)
    if y % g == 0:
        return 0
    else:
        return g - (y % g)

input_path = sys.argv[1]

with open(input_path, 'r') as input_file:

    n_cases = int(input_file.readline().strip())

    for case in xrange(1, n_cases+1):
        data = input_file.readline().strip().split()

        n_events = int(data[0])
        events_case = map(int, data[1:])

        solution = solve(events_case)

        print 'Case #{0}: {1}'.format(case, solution)
