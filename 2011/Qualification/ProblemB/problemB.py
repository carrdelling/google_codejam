#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2011
#
# Qualification round - Problem B - Magicka
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(combinations_list, destructions_list, invoke):

    spell = []

    for element in invoke:
        combining = False
        destructing = False
        if element in combinations_list and spell:
            last = spell[-1]
            if last in combinations_list[element]:
                spell = spell[:-1]
                spell.append(combinations_list[element][last])
                combining = True

        if not combining:
            if element in destructions_list:
                for element_2 in spell:
                    if element_2 in destructions_list[element]:
                        spell = []
                        destructing = True
                        continue

        if not combining and not destructing:
            spell.append(element)

    return '['+', '.join(spell)+']'


input_path = sys.argv[1]

with open(input_path, 'r') as input_file:

    n_cases = int(input_file.readline().strip())

    for case in xrange(1, n_cases+1):

        sequence = input_file.readline().strip().split()
        C = int(sequence[0])

        combinations = {}
        for i in xrange(0, C):
            comb = sequence[i+1]
            c_1 = comb[0]
            c_2 = comb[1]
            c_r = comb[2]
            if c_1 not in combinations:
                combinations[c_1] = {}
            combinations[c_1][c_2] = c_r

            if c_2 not in combinations:
                combinations[c_2] = {}
            combinations[c_2][c_1] = c_r

        D = int(sequence[C+1])

        destructions = {}
        for i in xrange(1, D+1):
            dest = sequence[C+1+i]
            d_1 = dest[0]
            d_2 = dest[1]

            if d_1 not in destructions:
                destructions[d_1] = []
            destructions[d_1].append(d_2)

            if d_2 not in destructions:
                destructions[d_2] = []
            destructions[d_2].append(d_1)

        N = int(sequence[C+D+2])

        invok = list(sequence[C+D+3])
        solution = solve(combinations, destructions, invok)

        print 'Case #{0}: {1}'.format(case, solution)
