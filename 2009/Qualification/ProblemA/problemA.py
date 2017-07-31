#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2009
#
# Qualification round - Problem A - Alien Language
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys

input_file = sys.argv[1]

with open(input_file, 'r') as input_f:
    header = input_f.readline()
    L, D, N = header.strip().split()
    L = int(L)
    D = int(D)
    N = int(N)

    dicts = [dict()] * L
    all_words = set()

    for i in range(L):
        dicts[i] = {}

    for i in range(D):
        word = input_f.readline().strip()

        for index, c in enumerate(word):
            if c not in dicts[index]:

                dicts[index][c] = set()

            dicts[index][c].add(word)
        all_words.add(word)

    for i in range(N):

        pattern = input_f.readline().strip()
        possible = set(all_words)

        position = 0
        multiple = []
        brackets = False
        for c in pattern:

            if c == '(':
                brackets = True
            elif c == ')':

                partial = set()
                for l in multiple:
                    if l in dicts[position]:
                        partial = partial | dicts[position][l]

                possible = possible & partial

                brackets = False
                multiple = []
                position += 1
            else:
                if not brackets:
                    if c in dicts[position]:
                        possible = possible & dicts[position][c]
                    else:
                        possible = set()
                    position += 1
                else:
                    multiple.append(c)

        print('Case #%d: %d' % (i + 1, len(possible)))
