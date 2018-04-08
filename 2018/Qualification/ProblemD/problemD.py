
################################################################################
#
# Google Code Jam - 2018
#
# Qualification round - Problem D - Cubic UFO
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

from math import sin, cos, pi, sqrt

EPSILON = 1e-7
SQRT_2 = sqrt(2)
SQRT_8 = sqrt(1/8)


def rotate_point_x(point, angle):
    x = point[0]
    y = (point[1] * cos(angle)) + (point[2] * -sin(angle))
    z = (point[1] * sin(angle)) + (point[2] * cos(angle))

    return x, y, z


def rotate_point_z(x, y, angle):
    x_ = x * cos(angle) - y * sin(angle)
    y_ = x * sin(angle) + y * cos(angle)

    return x_, y_


def close(a, b):
    return abs(a-b) < EPSILON


def compute_length(angle):

    return cos(angle) + sin(angle)


def compute_area(angle):
    r = cos(angle) * SQRT_2
    t = sin(angle)

    return r + t


def find_angle_large(target):

    min_angle = 0
    max_angle = 0.6155

    while True:
        current_angle = (min_angle + max_angle) / 2
        current_area = compute_area(current_angle)

        if close(target, current_area):
            return current_angle

        if current_area > target:
            max_angle = current_angle
        else:
            min_angle = current_angle


def solve_large(target):

    angle = find_angle_large(target)

    # initial points after first rotation
    p1 = (SQRT_8, SQRT_8, 0)
    p2 = (-SQRT_8, SQRT_8, 0)
    p3 = (0, 0, 0.5)

    # rotate in z axis, angle

    output = ['']
    output.append('{} {} {}'.format(*rotate_point_x(p1, angle)))
    output.append('{} {} {}'.format(*rotate_point_x(p2, angle)))
    output.append('{} {} {}'.format(*rotate_point_x(p3, angle)))

    return '\n'.join(output)


def find_angle_small(target):

    if target == 1.0:
        return 0

    if close(target, SQRT_2):
        return pi/4

    min_angle = 0
    max_angle = pi/4

    while True:
        current_angle = (min_angle + max_angle) / 2
        current_length = compute_length(current_angle)

        if close(target, current_length):
            return current_angle

        if current_length > target:
            max_angle = current_angle
        else:
            min_angle = current_angle


def solve_small(target):

    angle = find_angle_small(target)

    output = ['']

    # first point
    first = rotate_point_z(0.5, 0, angle)
    output.append('{} {} {}'.format(first[0], first[1], 0))

    # second point
    second = rotate_point_z(0, 0.5, angle)
    output.append('{} {} {}'.format(second[0], second[1], 0))

    # third point
    output.append('0 0 0.5')

    return '\n'.join(output)


def solve(target):

    if target <= SQRT_2:
        return solve_small(target)
    else:
        return solve_large(target)

if __name__ == "__main__":

    n_cases = int(input().strip())

    for case in range(1, n_cases + 1):
        target = float(input().strip())
        solution = solve(target)
        print('Case #{}: {}'.format(case, solution))
