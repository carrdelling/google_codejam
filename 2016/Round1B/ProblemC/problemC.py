#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2016
#
# Round 1B - Problem C - Technobabble
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys


def update_chain(graph, used, v, match):
    if used[v]:
        return False
    used[v] = True
    for to in graph[v]:
        if match[to] == -1 or update_chain(graph, used, match[to], match):
            match[to] = v
            return True
    return False


def solve(topics):

    left_words = {}
    right_words = {}
    index_left = 0
    index_right = 0

    for l, r in topics:
        if l not in left_words:
            left_words[l] = index_left
            index_left += 1
        if r not in right_words:
            right_words[r] = index_right
            index_right += 1

    # create a graph from left to right indexes [1: [2,4,6], 2: [1,2,6]]
    graph = [[] for _ in range(index_left)]
    for l, r in topics:
        x, y = left_words[l], right_words[r]
        graph[x].append(y)

    # match is an array of right to left  [2: 1, 1: 2] (every left is only taken once)
    # pre_used checks which left side items have been linked [1,2]
    match = [-1] * index_right
    pre_used = [False] * index_left
    for v in range(index_left):
        for to in graph[v]:
            if match[to] == -1:
                match[to] = v
                pre_used[v] = True
                break

    # for each left item unused, see if there is a right one that can be reached;
    # if so, update the chain of links
    for v in range(index_left):
        if pre_used[v]:
            continue
        used = [False] * index_left
        update_chain(graph, used, v, match)

    used_left, used_right = set(), set()
    minimum_cover = 0

    # 1: Add to minimum cover all the right nodes (add one edge for each)
    for to in range(index_right):
        v = match[to]
        used_left.add(v)
        used_right.add(to)
        minimum_cover += 1
    # 2: For each left node, if it was not used add it
    for v in range(index_left):
        if v not in used_left:
            minimum_cover += 1

    fake_topics = len(topics) - minimum_cover

    return fake_topics


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            n_topics = int(input_file.readline().strip())
            in_topics = []
            for topic in range(n_topics):
                in_topics.append(input_file.readline().strip().split())
            solution = solve(in_topics)
            print('Case #{}: {}'.format(case, solution))
