#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2010
#
# Qualification round - Problem C
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def trip(queue, capacity, memory):

    all_queue = sum(queue)

    if all_queue < capacity:
        return queue, all_queue

    signature = tuple(queue)

    if signature in memory:
        return memory[signature]

    inside = 0
    while inside+queue[0] <= capacity:
        inside += queue[0]
        queue = queue[1:] + queue[:1]

    memory[signature] = queue, inside

    return queue, inside


def solve(times, capacity, queue):

    profit = 0
    inner_memory = {}
    outer_memory = {}

    while times > 0:

        signature = tuple(queue)

        if signature not in outer_memory:
            outer_memory[signature] = profit, times
            queue, benefit = trip(queue, capacity, inner_memory)
            profit += benefit
            times -= 1
        else:
            old_profit, old_times = outer_memory[signature]
            lapse = old_times - times
            d_profit = profit - old_profit

            if lapse > times:
                outer_memory[signature] = profit, times
                queue, benefit = trip(queue, capacity, inner_memory)
                profit += benefit
                times -= 1
            else:
                cycles = times / lapse
                times -= cycles * lapse
                profit += cycles * d_profit

    return profit

input_path = sys.argv[1]

with open(input_path, 'r') as input_file:

    n_cases = int(input_file.readline().strip())

    for case in range(1, n_cases+1):

        r, k, n = map(int, input_file.readline().strip().split())
        whole_queue = map(int, input_file.readline().strip().split())

        solution = solve(r, k, whole_queue)

        print('Case #{0}: {1}'.format(case, solution))
