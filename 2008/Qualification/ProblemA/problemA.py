#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2008
#
# Qualification round - Problem A - Saving the Universe
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(_engines, _queries):

    all_engines = set(_engines)

    switches = 0

    available = set(all_engines)

    for q in _queries:

        if q in available:
            available.remove(q)

            if len(available) == 0:
                available = set(all_engines)
                available.remove(q)
                switches += 1

    return switches

if __name__ == '__main__':

    input_path = sys.argv[1]

    with open(input_path, 'r') as input_file:

        nCases = int(input_file.readline())

        for case in range(0, nCases):

            search = int(input_file.readline())
            engines = []

            for i in range(0, search):
                engines.append(input_file.readline().strip())

            Q = int(input_file.readline())
            queries = []

            for i in range(0, Q):
                queries.append(input_file.readline().strip())

            solution = solve(engines, queries)

            print('Case #%d: %d' % ((case+1), solution))
