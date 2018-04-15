#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2015
#
# Round1A - Problem C - Logging
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys
import bisect


def solve(trees):

    output = ['']

    for x, y in trees:

        up = 0
        down = 0

        left = []
        right = []

        # see how many trees are to the left and to the right - store the angles
        # also count how many trees are directly up and down

        for _x, _y in trees:

            if x == _x:
                if y > _y:
                    down += 1
                elif _y > y:
                    up += 1
            else:
                angle = (float(_y - y)/float(_x - x))
                if x > _x:
                    left.append(angle)
                else:
                    right.append(angle)

        left.sort()
        right.sort()

        # at most, we need to cut either all trees to the left or all trees to the right
        cut = min(len(left), len(right))

        for i, angle in enumerate(left):
            cut_after = down + len(left) - 1 - i + bisect.bisect_left(right, angle)
            cut_before = up + i + len(right) - bisect.bisect_right(right, angle)
            cut_angle = min(cut_after, cut_before)
            cut = min(cut_angle, cut)

        output.append(str(cut))

    return '\n'.join(output)


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            n = int(input_file.readline().strip())
            trees = []
            for _ in range(n):
                trees.append(map(int, input_file.readline().strip().split()))
            solution = solve(trees)
            print('Case #{}: {}'.format(case, solution))
