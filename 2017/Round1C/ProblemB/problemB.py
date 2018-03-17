#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2017
#
# Round 1C - Problem B - Parenting Partnering
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def solve(cameron, jamie):

    changes = 0

    activities = [(s, e, 'c') for s, e in cameron] + [(s, e, 'j') for s, e in jamie]
    activities.sort()

    # add 1 extra activity to account for the midnight period
    extra = list(activities[0])
    extra[0] += 1440
    extra[1] += 1440
    activities.append(extra)

    # generate a list of gaps (free time) and count the time served by each parent
    gaps = []
    parenting = {'c': 0, 'j': 0}

    # count also the time between tasks of the other parent (we want to avoid changes here)
    in_tasks_time = {'c': 0, 'j': 0}

    for i in range(len(activities) - 1):
        _prev = activities[i]
        _next = activities[i+1]

        is_free = 'c' if _prev[2] != 'c' else 'j'
        parenting[is_free] += _prev[1] - _prev[0]

        same_parent = _prev[2] == _next[2]
        length = _next[0] - _prev[1]
        code = is_free if same_parent else 'cj'

        # add only real gaps or real (forced) changes
        if length > 0 or is_free:
            gaps.append((length, code))

        if same_parent:
            in_tasks_time[is_free] += length

        gaps.sort()

    # find out who's the parent with less time assigned
    # (he will take as many full in between tasks as possible)
    most_free = 'c' if ((parenting['c'] + in_tasks_time['c']) <
                        (parenting['j'] + in_tasks_time['j'])) else 'j'
    less_free = 'c' if most_free == 'j' else 'j'

    # assign him all gaps where the other parent is busy both at the beginning at the end
    time_served = parenting[most_free]
    for gap in gaps:
        if gap[1] == most_free:
            time_served += gap[0]

            if time_served > 720:
                changes += 2

    # do the same for the other parent
    time_served = parenting[less_free]
    for gap in gaps:
        if gap[1] == less_free:
            time_served += gap[0]

            if time_served > 720:
                changes += 2

    # assign all the other gaps
    for gap in gaps:
        if gap[1] == 'cj':
            changes += 1

    return changes


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            C, J = map(int, input_file.readline().strip().split())

            c_activities = []
            j_activities = []

            for _ in range(C):
                start, end = map(int, input_file.readline().strip().split())
                c_activities.append((start, end))

            for _ in range(J):
                start, end = map(int, input_file.readline().strip().split())
                j_activities.append((start, end))

            solution = solve(c_activities, j_activities)
            print('Case #{}: {}'.format(case, solution))
