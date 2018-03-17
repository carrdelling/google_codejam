#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2017
#
# Round 1C - Problem C - Core Training
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys

EPSILON = 1e-5


def cum_prob(probabilities, required):
    sucesses = [1.0] + [0.] * required

    for p in probabilities:
        for i in range(required, 0, -1):
            sucesses[i] = ((1-p) * sucesses[i]) + (p * sucesses[i-1])

    return sucesses[required]


def solve_subset(probabilities, required, energy):

    subset_solution = cum_prob(probabilities, required)

    # try to fill in a subset of the units with energy
    # we are interested only in subsets that end up with the same energy in every unit and
    # no more energy than the next one

    for i in range(len(probabilities)):
        initial_energy = 0.0
        for j in range(i, len(probabilities)):
            initial_energy += probabilities[j]

            new_unit_power = (initial_energy+energy)/float(j-i+1)

            # we cannot assign the same energy to all of them
            if new_unit_power < probabilities[j]:
                continue

            # we would assign more probability to this group than to the following one
            if j < len(probabilities) - 1 and new_unit_power > probabilities[j+1] - EPSILON:
                continue

            new_unit_power = min(new_unit_power, 1.0)
            new_configuration = probabilities[:i]+[new_unit_power]*(j-i+1)+probabilities[j+1:]
            subset_solution = max(subset_solution, cum_prob(new_configuration, required))

    return subset_solution


def solve(required, energy, probabilities):

    output = solve_subset(probabilities, required, energy)

    # try to improve the solution if we fill completely the last (higher probability) unit
    while probabilities:
        if probabilities[-1] + energy < 1.0:
            break

        energy -= 1.0 - probabilities[-1]
        required = required - 1 if required > 0 else 0
        probabilities = probabilities[:-1]

        new_output = solve_subset(probabilities, required, energy)
        output = max(output, new_output)

    return output


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            N, K = map(int, input_file.readline().strip().split())
            U = float(input_file.readline().strip())
            units = sorted(map(float, input_file.readline().strip().split()))

            solution = solve(K, U, units)
            print('Case #{}: {:.9f}'.format(case, solution))
