from copy import copy
from collections import Counter


def serialize_keys(counter):

    return ''.join(['{}{}'.format(key, counter[key]) for key in sorted(counter)])


def serialize_chests(_chests):

    all_str = []

    for ch in _chests:
        inside = ''.join([x for x in ch[2]])
        _str = '{}{}{}'.format(ch[0], ch[1], inside)
        all_str.append(_str)

    return 'X'.join(all_str)


def check_feasible(fea_keys, fea_chests):

    removed = True

    while removed:
        removed = False
        for chest in fea_chests[:]:
            if fea_keys.get(chest[1], 0) > 0:
                for k in chest[2]:
                    fea_keys[k] += 1
                fea_chests.remove(chest)
                removed = True

    return not fea_chests


def solve(keys, chests, memo):

    if len(chests) == 1:
        if keys.get(chests[0][1], 0) > 0:
            return [chests[0][0]]
        else:
            return "IMPOSSIBLE"

    str_keys = serialize_keys(keys)
    str_chests = serialize_chests(chests)

    if (str_keys, str_chests) in memo:
        return memo[(str_keys, str_chests)]

    fea_keys = copy(keys)
    fea_chests = copy(chests)
    if not check_feasible(fea_keys, fea_chests):
        return "IMPOSSIBLE"

    for idx in range(len(chests)):

        if keys.get(chests[idx][1], 0) < 1:
            continue

        new_keys = copy(keys)
        new_keys[chests[idx][1]] -= 1

        for k in chests[idx][2]:
            new_keys[k] += 1

        new_chests = chests[:idx] + chests[idx+1:]
        solution = solve(new_keys, new_chests, memo)

        memo[(str_keys, str_chests)] = solution
        if solution == "IMPOSSIBLE":
            continue

        return [chests[idx][0]] + solution

    return "IMPOSSIBLE"


def start_solve(initial_keys, chests, memo):

    ava_keys = copy(initial_keys)

    for c in chests:
        for k in c[2]:
            ava_keys[k] += 1
        ava_keys[c[1]] -= 1

    for k in ava_keys:
        if ava_keys[k] < 0:
            return "IMPOSSIBLE"

    return solve(initial_keys, chests, memo)


if __name__ == "__main__":

    with open('input2.txt') as input_file:

        cases = int(input_file.readline())

        for c in range(cases):

            n_keys, n_chests = map(int, input_file.readline().split())
            initial_keys = Counter(input_file.readline().split())

            chests = []
            for i in range(n_chests):
                lock, _, *keys = input_file.readline().split()
                chests.append((i+1, lock, keys))

            memo = {}
            solution = start_solve(initial_keys, chests, memo)

            if solution != "IMPOSSIBLE":
                solution = ' '.join([str(x) for x in solution])
            print('Case #{}: {}'.format(c+1, solution))
