#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2017
#
# Round1A - Problem C - Play the Dragon
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################


import sys
from math import ceil, log2


def attack_turns(attack, knight, buff):

    # turns to kill the knight
    current_attack = attack
    n_bufs = 0
    turns = int(ceil(knight / current_attack)) + n_bufs
    best_turns = None

    while not best_turns or turns <= best_turns:
        best_turns = turns
        current_attack += buff
        n_bufs += 1
        turns = int(ceil(knight / current_attack)) + n_bufs

    return best_turns


def solve(dragon, attack, knight, damage, buff, debuff):

    offense = attack_turns(attack, knight, buff)

    # if the dragon does not need to cure/debuff
    if offense <= int(ceil(dragon / damage)):
        return offense

    # if the knight kills the dragon in the first turn anyway
    if knight > attack and damage - debuff >= dragon:
        return 'IMPOSSIBLE'

    # if the dragon cannot debuff
    if debuff == 0:
        # for how many turns can the dragon stand on (at least 1HP)?
        survive = (dragon-1) // damage
        free_actions = survive - 1

        if survive < 2 and knight > attack:
            return 'IMPOSSIBLE'
        else:
            # the dragon has 2 extra turns at the beggining (first + knight killing strike)
            # and 1 extra at the end (knight killing strike)
            defense = (offense - 3) // free_actions
            return offense + defense

    MAX_ANSWER = 1e15
    best = MAX_ANSWER
    current_defense = 0
    cured_last_turn = False
    current_hp = dragon
    free_actions = -1

    # keep debuffing until the knight has no damage power - save the best (fastest) solution
    while damage > 0:

        # total number of offensive actions allowed at this debuff level
        last_free_actions = free_actions
        free_actions = ((dragon-1) // damage) - 1

        # current amount of hits the dragon can withstand
        survive = (current_hp - 1) // damage

        # if the dragon does not need to cure (turns to Hp=1 + 1 extra turn)
        if offense <= survive + 1:
            best = min(best, current_defense + offense)

        # if the dragon will need healing, but this iteration gives more room
        # for enough offensive actions
        elif free_actions > max(0, last_free_actions) and not cured_last_turn:

            total_cost = current_defense
            total_cost += offense

            # turns healing
            total_cost += 1 + ((offense - survive - 2) // free_actions)
            best = min(best, total_cost)

        # if the next dragon action should be healing
        if current_hp <= damage - debuff:
            # if the dragon healed before, there is no way he can do better - stop debuffing
            if cured_last_turn:
                break

            # heal
            current_defense += 1
            cured_last_turn = True

            # get the next hit from the knight
            current_hp = dragon - damage

            if free_actions > 0:
                # try to apply multiple (2,4,8,16,32,64 ...) debuffs at once
                max_exp_r = int(log2(ceil(damage/debuff))) - 1

                for total_debuffs in [2 ** x for x in range(max_exp_r, 0, -1)]:
                    # see how many debuffs the dragon need to apply per round
                    # for a given number of debuffs
                    debuffs_per_round = ((dragon - 1) // (damage - total_debuffs * debuff)) - 1
                    if free_actions >= debuffs_per_round:
                        cycles = total_debuffs // free_actions
                        current_defense += cycles * (free_actions + 1)
                        damage -= cycles * free_actions * debuff
                        current_hp = dragon - damage
                        break
        else:
            cured_last_turn = False
            current_defense += 1
            damage -= debuff
            current_hp -= damage
    else:
        # in some rare cases, the dragon may save itself by debuffing the knight to 0 in a single
        # round (even if debuffing should not work). This check takes care of it
        best = min(best, current_defense + offense)

    return best if best < MAX_ANSWER else 'IMPOSSIBLE'

if __name__ == "__main__":

    input_path = sys.argv[1]

    with open(input_path) as input_file:

        n_cases = int(input_file.readline().strip())

        for case in range(1, n_cases+1):
            hd, ad, hk, ak, b, d = map(int, input_file.readline().strip().split())
            solution = solve(hd, ad, hk, ak, b, d)
            print('Case #{0}: {1}'.format(case, solution))
