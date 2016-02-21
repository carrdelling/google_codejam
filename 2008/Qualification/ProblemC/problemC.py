#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2008
#
# Qualification round - Problem C - Fly swatter
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

from math import pi, acos, asin, sqrt, ceil
import sys


def area_up_left(x, y, rad):

    if x < rad and y < rad:

        a = rad * rad * (acos(x / rad) - asin(y / rad))

        if a <= 0.0:
            return 0.0
        else:
            a += (2.0 * x * y - y * sqrt(rad * rad - y * y) -
                  x * sqrt(rad * rad - x * x))
            return a / 2.0
    else:
        return 0.0


def square_area(lx, ly, a, rad):

    if lx >= rad or ly >= rad:
        return 0.0

    ux = lx + a
    uy = ly + a

    if lx * lx + ly * ly >= rad * rad:
        return 0.0

    elif ux * ux + uy * uy <= rad * rad:
        return a * a
    else:
        return area_up_left(lx, ly, rad) - area_up_left(ux, ly, rad) \
               - area_up_left(lx, uy, rad) + area_up_left(ux, uy, rad)


def solve(_f, rr, _t, rad, _g):

    n = int(ceil((rr + _g) / (2.0 * rad + _g)))

    a = _g - 2.0 * _f

    if a <= 0.0:
        return 1.0

    area = 0.0

    for i in xrange(0, n):
        for j in xrange(0, n):
            area += square_area(rad + _f + (2.0 * rad + _g) * i,
                                rad + _f + (2.0 * rad + _g) * j, a, rr - _t - _f)

    output = 1.0 - 4.0 * area / (pi * rr * rr)

    return output


if __name__ == '__main__':

    input_path = sys.argv[1]

    with open(input_path, 'r') as input_file:

        nCases = int(input_file.readline())

        for case in xrange(0, nCases):
            f, r, t, _r, g = map(float, input_file.readline().strip().split())

            solution = solve(f, r, t, _r, g)

            print 'Case #%d: %.6f' % ((case + 1), solution)
