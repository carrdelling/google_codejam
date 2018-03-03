#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2016
#
# Round 1C - Problem B - Slides!
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(buildings, ways):

    if ways > 2 ** (buildings - 2):
        return "IMPOSSIBLE"

    if buildings == 2:
        output = ["POSSIBLE", "01", "00"]
        return '\n'.join(output)

    full_set = ways == 2 ** (buildings - 2)

    mask = bin(ways - 1)[2:] if full_set else bin(ways)[2:]
    padding_zeroes = buildings - 2 - len(mask)
    full_mask = '0' * padding_zeroes + mask

    first_building = '0' + full_mask

    first_building += '1' if full_set else '0'

    output = ["POSSIBLE", first_building]

    for building in range(1, buildings - 1):
        new_building = '0' * (building + 1) + '1' * (buildings - building - 1)
        output.append(new_building)
    else:
        output.append('0' * buildings)

    return '\n'.join(output)


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            B, M = map(int, input_file.readline().strip().split())

            solution = solve(B, M)
            print('Case #{}: {}'.format(case, solution))
