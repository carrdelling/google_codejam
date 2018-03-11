#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2017
#
# Round1A - Problem B - Ratatouille
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys
from math import floor, ceil
from collections import defaultdict


MAX_SERVINGS = 1000000


def solve(n_ingredients, targets, sources):

    ingredients = defaultdict(list)
    for ingredient, weights in enumerate(sources):
        for w in weights:
            min_i = max(1, int(floor(w / (targets[ingredient] * 1.1))))
            max_i = int(ceil(w / (targets[ingredient] * 0.9))) + 1
            servings = [i for i in range(min_i, max_i)
                        if 0.9 <= (w / (targets[ingredient] * i)) <= 1.1]

            if not servings:
                continue
            min_servings, max_servings = min(servings), max(servings)
            ingredients[ingredient].append((min_servings, max_servings))

    for ingredient in ingredients:
        ingredients[ingredient].sort()

    n_kits = 0

    while all(len(ingredients[ingredient]) > 0 for ingredient in range(n_ingredients)):

        # pick the ingredient with the minimum maximum
        min_max = ingredients[0][0][1]
        current_ingredient = 0
        for ingredient in range(1, n_ingredients):
            if ingredients[ingredient][0][1] < min_max:
                min_max = ingredients[ingredient][0][1]
                current_ingredient = ingredient

        # see if a kit can be formed
        min_servings, max_servings = ingredients[current_ingredient][0]
        for ingredient in range(n_ingredients):
            other_min, other_max = ingredients[ingredient][0]

            # ingredient servings do not match
            if not (min_servings <= other_max and max_servings >= other_min):
                # drop the minimum ingredient (it is useless)
                ingredients[current_ingredient] = ingredients[current_ingredient][1:]
                break
        else:
            # all ingredient servings match - use them to create a kit
            for type_ingredient in ingredients:
                ingredients[type_ingredient] = ingredients[type_ingredient][1:]
            n_kits += 1

    return n_kits


if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:
        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            n_ing, n_packages = map(int, input_file.readline().strip().split())
            requirements = list(map(float, input_file.readline().strip().split()))
            packages = []
            for row in range(n_ing):
                wg = list(map(float, input_file.readline().strip().split()))
                packages.append(wg)
            solution = solve(n_ing, requirements, packages)
            print('Case #{}: {}'.format(case, solution))
