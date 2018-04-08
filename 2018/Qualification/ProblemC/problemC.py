################################################################################
#
# Google Code Jam - 2018
#
# Qualification round - Problem C - Go, Gopher!
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################


def count_empty(field, col):
    return len(field[col - 1]) + len(field[col]) + len(field[col + 1])


def gopher(chosen_column):
    # note that judge columns are 1-indexes, whereas ours are 0-indexed

    row = 2
    column = chosen_column + 1

    print('{} {}'.format(row, column))
    answer = input()

    row, col = map(int, answer.strip().split())
    col -= 1

    return row, col


def solve(area):

    length = (area // 3) + 1
    to_excavate = [{1, 2, 3} for _ in range(length)]

    tries = 0
    while True:

        # choose target column
        max_empty = count_empty(to_excavate, 1)
        chosen = 1
        for i in range(2, length-1):
            _empty = count_empty(to_excavate, i)
            if _empty > max_empty:
                chosen = i
                max_empty = _empty

        # send the gopher
        row, col = gopher(chosen)
        tries += 1

        # annotate the outcome
        if row == -1:
            break

        if row == 0:
            break

        to_excavate[col].discard(row)


if __name__ == "__main__":

    n_cases = int(input().strip())

    for case in range(1, n_cases + 1):
        A = int(input().strip())
        solve(A)
