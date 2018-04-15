#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2015
#
# Round1B - Problem C - Hiking Deer
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys
import heapq


def solve(hikers):

    # put all hikers in a priority queue, sorted by next time they will reach the start
    schedule = []
    for d, h, m in hikers:

        for j in range(h):
            m_ = m + j
            time_next = (360 - d) * m_
            cycle_time = 360 * m_
            heapq.heappush(schedule, (time_next, cycle_time))

    # the best solution is having all the hikers passing once
    best = current = len(schedule)

    # here we store already processed hikers, how may come again to the start (too soon!)
    passed = []

    # while is possible to improve the answer
    while current - len(schedule) < best:
        # if the next hiker reaching the start is a 'new' one
        if not passed or schedule[0][0] < passed[0][0]:
            time_next, cycle_time = heapq.heappop(schedule)

            # we can arrive after him - and avoid crossing him
            current -= 1
            if current < best:
                best = current

        else:

            # if the next hiker reaching the start is an 'old' one
            time_next, cycle_time = heapq.heappop(passed)

            # then we have to cross him twice (thrice...)
            current += 1

        # put the hiker in the already processed queue with its new time
        time_next += cycle_time
        heapq.heappush(passed, (time_next, cycle_time))

    return best


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())
        for case in range(1, n_cases+1):
            n_groups = int(input_file.readline().strip())
            hikers = []
            for _ in range(n_groups):
                position, number, fastest = map(int, input_file.readline().strip().split())
                hikers.append((position, number, fastest))
            solution = solve(hikers)
            print('Case #{}: {}'.format(case, solution))
