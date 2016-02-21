#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2009
#
# Qualification round - Problem B - Watersheds
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys

input_file = sys.argv[1]

with open(input_file, 'r') as input_f:
    T = int(input_f.readline().strip())

    for case in xrange(1, T + 1):

        H, W = input_f.readline().strip().split()
        H = int(H)
        W = int(W)

        t_map = [[]] * H

        for row in xrange(0, H):
            data = input_f.readline().strip().split()
            t_map[row] = [int(x) for x in data]

        f_map = []

        for row in xrange(0, H):

            f_map.append([-1] * W)

        for x in xrange(0, H):
            for y in xrange(0, W):

                ground = t_map[x][y]
                f_map[x][y] = 0

                # north

                if x > 0 and t_map[x - 1][y] < ground:
                    ground = t_map[x - 1][y]
                    f_map[x][y] = 1

                # west

                if y > 0 and t_map[x][y - 1] < ground:
                    ground = t_map[x][y - 1]
                    f_map[x][y] = 2

                # east
                if y < W - 1 and t_map[x][y + 1] < ground:
                    ground = t_map[x][y + 1]
                    f_map[x][y] = 3

                # south

                if x < H - 1 and t_map[x + 1][y] < ground:
                    ground = t_map[x + 1][y]
                    f_map[x][y] = 4

        label = 'a'
        for x in xrange(0, H):
            for y in xrange(0, W):
                if f_map[x][y] == 0:
                    f_map[x][y] = label
                    order = ord(label) + 1
                    label = chr(order)

        not_full = True
        while not_full:
            not_full = False
            for x in xrange(0, H):
                for y in xrange(0, W):
                    if f_map[x][y] not in [1, 2, 3, 4]:

                        # north
                        if x > 0 and f_map[x - 1][y] == 4:
                            f_map[x - 1][y] = f_map[x][y]
                            not_full = True

                        # west
                        if y > 0 and f_map[x][y - 1] == 3:
                            f_map[x][y - 1] = f_map[x][y]
                            not_full = True

                        # east
                        if y < W - 1 and f_map[x][y + 1] == 2:
                            f_map[x][y + 1] = f_map[x][y]
                            not_full = True

                        # south
                        if x < H - 1 and f_map[x + 1][y] == 1:
                            f_map[x + 1][y] = f_map[x][y]
                            not_full = True

        translate = {}
        label2 = 'a'
        for x in xrange(0, H):
            for y in xrange(0, W):
                if f_map[x][y] not in translate:
                    translate[f_map[x][y]] = label2
                    label2 = chr(ord(label2) + 1)

        for x in xrange(0, H):
            for y in xrange(0, W):
                f_map[x][y] = translate[f_map[x][y]]

        print 'Case #%d:' % case
        for x in xrange(0, H):
            print ' '.join(f_map[x])
