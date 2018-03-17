#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2017
#
# Round 1B - Problem B - Stable Neigh-bors
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


options = {'R': ['Y', 'B'],
           'Y': ['R', 'B'],
           'B': ['Y', 'R'],
          }


def get_max_basic(counts, avoid=''):

    avoid = list(avoid)

    options = [(k, v) for k, v in counts.items() if k not in avoid]

    chosen = next(iter(sorted(options, key=lambda x:x[1], reverse=True)))

    if counts[chosen[0]] <= 1:
        counts.pop(chosen[0])
    else:
        counts[chosen[0]] -= 1

    return chosen


def solve_RYB(counts):

    solution = ''

    best_horse, count = get_max_basic(counts)

    n = sum(counts.values()) + 1

    if count * 2 > n:
        return 'IMPOSSIBLE'

    solution += best_horse

    while counts:
        if solution[-1] == best_horse:
            avoid = best_horse
            next_horse, count = get_max_basic(counts, avoid=avoid)
        elif best_horse in counts:
            next_horse = best_horse
            if counts[best_horse] <= 1:
                counts.pop(best_horse)
            else:
                counts[best_horse] -= 1
        else:
            avoid = solution[-1]
            next_horse, count = get_max_basic(counts, avoid=avoid)

        solution += next_horse

    return solution


def solve(counts):

    counts = {k: v for k, v in counts.items() if v > 0}

    if len(counts) < 2:
        return 'IMPOSSIBLE'

    new_counts = {}

    if 'G' in counts:
        if len(counts) > 2:
            if counts.get('R', 0) >= counts['G'] + 1:
                new_counts['R'] = counts['R'] - counts['G']
            else:
                return 'IMPOSSIBLE'
        elif counts.get('R', 0) == counts['G']:
            return 'RG' * counts['G']
        else:
            return 'IMPOSSIBLE'
    elif 'R' in counts:
        new_counts['R'] = counts['R']

    if 'O' in counts:
        if len(counts) > 2:
            if counts.get('B', 0) >= counts['O'] + 1:
                new_counts['B'] = counts['B'] - counts['O']
            else:
                return 'IMPOSSIBLE'
        elif counts.get('B', 0) == counts['O']:
            return 'BO' * counts['O']
        else:
            return 'IMPOSSIBLE'
    elif 'B' in counts:
        new_counts['B'] = counts['B']

    if 'V' in counts:
        if len(counts) > 2:
            if counts.get('Y', 0) >= counts['V'] + 1:
                new_counts['Y'] = counts['Y'] - counts['V']
            else:
                return 'IMPOSSIBLE'
        elif counts.get('Y', 0) == counts['V']:
            return 'YV' * counts['V']
        else:
            return 'IMPOSSIBLE'
    elif 'Y' in counts:
        new_counts['Y'] = counts['Y']

    partial_solution = solve_RYB(new_counts)

    if partial_solution == 'IMPOSSIBLE':
        return 'IMPOSSIBLE'

    solution = ''
    for horse in partial_solution:

        while horse == 'R' and counts.get('G', 0) > 0:
            counts['G'] -= 1
            solution += 'RG'

        while horse == 'Y' and counts.get('V', 0) > 0:
            counts['V'] -= 1
            solution += 'YV'

        while horse == 'B' and counts.get('O', 0) > 0:
            counts['O'] -= 1
            solution += 'BO'

        solution += horse

    return solution


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:

        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            counts = list(map(int, input_file.readline().strip().split()))
            counts = {
                      'R': counts[1],
                      'O': counts[2],
                      'Y': counts[3],
                      'G': counts[4],
                      'B': counts[5],
                      'V': counts[6]
            }

            solution = solve(counts)
            print('Case #{0}: {1}'.format(case, solution))
