#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2016
#
# Round 1B - Problem B - Close Match
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def value(s):
    return ord(s) - 48


def search(a, b, prefix_a, prefix_b):

    # if we have processed the whole number, return (diff, int(coders), int(jammers))
    # (for sorting the solutions out)
    if not a:
        return abs(int(prefix_a) - int(prefix_b)), int(prefix_a), int(prefix_b)

    options = []

    # if prefixes are equal or we are starting
    if not prefix_a or (int(prefix_a) == int(prefix_b)):
        # if both current positions are ?, try using 0's and 1's
        if a[0] == '?' and b[0] == '?':
            new_options = [(prefix_a + '0', prefix_b + '0'), (prefix_a + '0', prefix_b + '1'),
                           (prefix_a + '1', prefix_b + '0'), (prefix_a + '1', prefix_b + '1')]

        # if only current position for a is ?, try to fit numbers close to b
        elif a[0] == '?' and b[0] != '?':
            b_value = value(b[0])

            new_options = [(prefix_a + b[0], prefix_b + b[0])]

            if b_value < 9:
                new_options.append((prefix_a + str(b_value + 1), prefix_b + b[0]))
            if b_value > 0:
                new_options.append((prefix_a + str(b_value - 1), prefix_b + b[0]))

        # if only current position for b is ?, try to fit numbers close to a
        elif a[0] != '?' and b[0] == '?':
            a_value = value(a[0])

            new_options = [(prefix_a + a[0], prefix_b + a[0])]

            if a_value < 9:
                new_options.append((prefix_a + a[0], prefix_b + str(a_value + 1)))

            if a_value > 0:
                new_options.append((prefix_a + a[0], prefix_b + str(a_value - 1)))

        # if there are no ? in the current positions
        else:
            # continue solving
            new_options = [(prefix_a + a[0], prefix_b + b[0])]

        # search in all the new options found
        for opt in new_options:
            options.append(search(a[1:], b[1:], opt[0], opt[1]))

    # if the a prefix is higher, replace ? with 0's on a, and with 9's on b
    elif int(prefix_a) > int(prefix_b):

        if a[0] == '?' and b[0] == '?':
            options.append(search(a[1:], b[1:], prefix_a + '0', prefix_b + '9'))
        if a[0] == '?' and b[0] != '?':
            options.append(search(a[1:], b[1:], prefix_a + '0', prefix_b + b[0]))
        if a[0] != '?' and b[0] == '?':
            options.append(search(a[1:], b[1:], prefix_a + a[0], prefix_b + '9'))
        if a[0] != '?' and b[0] != '?':
            options.append(search(a[1:], b[1:], prefix_a + a[0], prefix_b + b[0]))

    # if the b prefix is higher, replace ? with 0's on b, and with 9's on a
    elif int(prefix_a) < int(prefix_b):
        if a[0] == '?' and b[0] == '?':
            options.append(search(a[1:], b[1:], prefix_a + '9', prefix_b + '0'))
        if a[0] == '?' and b[0] != '?':
            options.append(search(a[1:], b[1:], prefix_a + '9', prefix_b + b[0]))
        if a[0] != '?' and b[0] == '?':
            options.append(search(a[1:], b[1:], prefix_a + a[0], prefix_b + '0'))
        if a[0] != '?' and b[0] != '?':
            options.append(search(a[1:], b[1:], prefix_a + a[0], prefix_b + b[0]))

    options.sort()

    return options[0]


def solve(a, b):

    best_solution = search(a, b, '', '')

    coders = str(best_solution[1]).zfill(len(a))
    jammers = str(best_solution[2]).zfill(len(b))

    return coders, jammers


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())
        for case in range(1, n_cases+1):
            team_a, team_b = input_file.readline().strip().split()
            solution = solve(team_a, team_b)
            print('Case #{}: {} {}'.format(case, solution[0], solution[1]))
