################################################################################
#
# Google Code Jam - 2018
#
# Qualification round - Problem B - Trouble Sort
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################


LARGE_VALUE = 1e9 + 1


def solve(original):

    if len(original) % 2 == 1:
        original.append(LARGE_VALUE)

    even = sorted(original[::2])
    odd = sorted(original[1::2])

    if even[0] > odd[0]:
        return 0

    for idx, i in enumerate(even[1:], 1):
        if i < odd[idx-1]:
            return (idx * 2) - 1
        if i > odd[idx]:
            return idx * 2

    return "OK"


if __name__ == "__main__":

    n_cases = int(input().strip())

    for case in range(1, n_cases + 1):
        _ = input()
        values = list(map(int, input().strip().split()))
        solution = solve(values)
        print('Case #{0}: {1}'.format(case, solution))
