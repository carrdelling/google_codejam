#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2017
#
# Round 1B - Problem C - Pony Express
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys

MAX_VALUE = 1e50


def solve_small(N, horses, distances):

    best_path = [MAX_VALUE] * N
    best_path[0] = 0.0

    for city in range(N - 1):

        energy, speed = horses[city]
        current_cost = best_path[city]
        for target in range(city+1, N):

            distance = distances[(target-1, target)]
            energy -= distance

            cost = float(distance) / float(speed) if energy >= 0 else MAX_VALUE

            current_cost += cost

            best_path[target] = min(best_path[target], current_cost)

            if energy < 0:
                break

    return best_path[-1]


def minimize(graph, N):

    new_graph = dict(graph)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                new_graph[(i, j)] = min(new_graph[(i, j)], new_graph[(i, k)] + new_graph[(k, j)])

    return new_graph


def solve(N, horses, distances, quests):

    # Transform -1 path into infinite distances
    for k, v in distances.items():
        distances[k] = v if v >= 0 else MAX_VALUE

    # minimize distances
    min_distances = minimize(distances, N)

    # transform the distances into horse costs
    horse_costs = {}
    for i in range(N):
        energy, speed = horses[i]
        for j in range(N):
            horse_costs[(i, j)] = (min_distances[(i, j)] / float(speed)) if energy >= min_distances[(i, j)] else MAX_VALUE

    # minimize costs
    min_costs = minimize(horse_costs, N)

    # compute output
    output = []
    for start, finish in quests:
        cost = min_costs[(start, finish)]
        output.append(cost)

    return ' '.join(map(str, output))


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            N, Q = map(int, input_file.readline().strip().split())

            horses = {}
            for i in range(N):
                E, S = map(int, input_file.readline().strip().split())
                horses[i] = (E, S)

            distances = {}
            for i in range(N):
                i_distances = list(map(int, input_file.readline().strip().split()))
                for j in range(N):
                    distances[(i, j)] = i_distances[j]

            quests = []
            for _ in range(Q):
                S, F = map(int, input_file.readline().strip().split())
                quests.append((S - 1, F - 1))

            solution = solve(N, horses, distances, quests)
            print('Case #{}: {}'.format(case, solution))
