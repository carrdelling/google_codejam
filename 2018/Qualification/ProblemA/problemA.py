################################################################################
#
# Google Code Jam - 2018
#
# Qualification round - Problem A - Saving The Universe Again
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################


def solve(life, commands):

    dmg = {}

    current = 1
    for c in commands:
        if c == 'S':
            dmg[current] = dmg.get(current, 0) + 1
        if c == 'C':
            current *= 2

    if life < sum(dmg.values()):
        return "IMPOSSIBLE"

    hacks = 0
    while sum(k * v for k, v in dmg.items()) > life:
        pos = max(dmg)

        if dmg[pos] == 1:
            dmg.pop(pos)
        else:
            dmg[pos] -= 1

        dmg[pos//2] = dmg.get(pos//2, 0) + 1
        hacks += 1

    return hacks


if __name__ == "__main__":

    n_cases = int(input().strip())

    for case in range(1, n_cases + 1):
        D, S = input().strip().split()
        solution = solve(int(D), S)
        print('Case #{0}: {1}'.format(case, solution))
