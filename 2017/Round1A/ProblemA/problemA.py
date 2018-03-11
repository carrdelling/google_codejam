#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2017
#
# Round1A - Problem A - Alphabet Cake
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def fill_columnwise(r, c, grid):

    remaining = True
    advancing = True

    while remaining and advancing:
        remaining = False
        advancing = False
        for i in range(r):
            for j in range(c):

                if grid[i][j] == '?':

                    # look above
                    if i > 0 and grid[i - 1][j] != '?':
                        grid[i][j] = grid[i - 1][j]
                        advancing = True
                    # look below
                    elif i < r - 1 and grid[i + 1][j] != '?':
                        grid[i][j] = grid[i + 1][j]
                        advancing = True
                    # mark as unsolved
                    else:
                        remaining = True

    return remaining


def solve(r, c, grid):

    for i, row in enumerate(grid):
        grid[i] = list(row[0])

    remaining = fill_columnwise(r, c, grid)

    if remaining:
        # transpose to fill row wise this time
        # this works because we are guaranted to have a full column at least

        grid = list(map(list, zip(*grid)))
        fill_columnwise(c, r, grid)
        grid = list(map(list, zip(*grid)))

    output = '\n'.join(''.join(row) for row in grid)

    return output


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:

        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            rows, cols = map(int, input_file.readline().strip().split())
            cake = []
            for _ in range(rows):
                cake.append(list(input_file.readline().strip().split()))
            solution = solve(rows, cols, cake)
            print('Case #{0}: \n{1}'.format(case, solution))
