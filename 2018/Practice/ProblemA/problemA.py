################################################################################
#
# Google Code Jam - 2018
#
# Practice session - Problem A - Number guessing
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################


import sys


def solve(A, B):

    print("Case {}. Limits are {} <--> {}".format(case, A, B), file=sys.stderr)
    while True:
        guess = (A + B + 1) // 2

        print(">> Sending {}".format(guess), file=sys.stderr)
        print(guess)

        answer = input().strip()
        print("> Got back: {}".format(answer), file=sys.stderr)

        if answer == 'CORRECT':
            break

        if answer == 'WRONG_ANSWER':
            break

        if answer == 'TOO_SMALL':
            if guess == B - 1:
                A = B
            else:
                A = guess

        if answer == 'TOO_BIG':
            B = guess

if __name__ == "__main__":

    n_cases = int(input().strip())

    for case in range(1, n_cases + 1):
        A, B = map(int, input().strip().split())
        N = int(input().strip())
        solve(A, B)
