################################################################################
#
# Google Code Jam - 2017
#
# Practice session - Problem C - Steed 2: Cruise Control
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################


def solve(D, horses):

    # time for the slowest horse
    slowest = 0

    for h in horses:
        time = (D - h[0])/h[1]
        slowest = max(slowest, time)

    # speed to arrive at the same time of the slowest horse
    speed = D/slowest

    return round(speed, 7)

if __name__ == "__main__":

    n_cases = int(input().strip())

    for case in range(1, n_cases+1):
        D, N = list(map(int, input().strip().split()))

        horses = []

        for _ in range(N):
            horse = list(map(int, input().strip().split()))
            horses.append(horse)

        solution = solve(D, horses)
        print('Case #{0}: {1}'.format(case, solution))
