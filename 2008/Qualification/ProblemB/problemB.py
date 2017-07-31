#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2008
#
# Qualification round - Problem B - Train Timetable
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################


from datetime import datetime, timedelta
import sys


def solve(turnover, trip_a, trip_b):

    initial_trains_a = 0
    initial_trains_b = 0
    available_a = 0
    available_b = 0

    trips = []

    for t in trip_a:
        start, end = t.strip().split()
        start = datetime.strptime(start, '%H:%M')
        end = datetime.strptime(end, '%H:%M')
        trips.append((start, end, 'A'))

    for t in trip_b:
        start, end = t.strip().split()
        start = datetime.strptime(start, '%H:%M')
        end = datetime.strptime(end, '%H:%M')
        trips.append((start, end, 'B'))

    trips.sort(key=lambda x: x[0], reverse=True)

    while len(trips) > 0:

        t = trips.pop()

        if t[2] == 'A':

            if available_a < 1:
                initial_trains_a += 1
                available_a += 1

            available_a -= 1
            free = t[1] + timedelta(minutes=turnover-1) + timedelta(seconds=1)

            trips.append((free, free, '-B'))
            trips.sort(key=lambda x: x[0], reverse=True)

        if t[2] == 'B':
            if available_b < 1:
                initial_trains_b += 1
                available_b += 1

            available_b -= 1
            free = t[1] + timedelta(minutes=turnover-1) + timedelta(seconds=1)

            trips.append((free, free, '-A'))
            trips.sort(key=lambda x: x[0], reverse=True)

        if t[2] == '-A':

            available_a += 1

        if t[2] == '-B':

            available_b += 1

    return initial_trains_a, initial_trains_b

if __name__ == '__main__':

    input_path = sys.argv[1]

    with open(input_path, 'r') as input_file:

        nCases = int(input_file.readline())

        for case in range(0, nCases):

            turnover_value = int(input_file.readline())
            A, B = input_file.readline().strip().split()

            A, B = int(A), int(B)

            trip_a_list = []
            trip_b_list = []

            for i in range(A):
                time = input_file.readline().strip()
                trip_a_list.append(time)

            for i in range(B):
                time = input_file.readline().strip()
                trip_b_list.append(time)

            solution_A, solution_B = solve(turnover_value, trip_a_list,
                                           trip_b_list)

            print('Case #%d: %d %d' % ((case+1), solution_A, solution_B))
