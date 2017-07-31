#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2009
#
# Qualification round - Problem C - Welcome to Code Jam
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################
import sys


input_path = sys.argv[1]

pattern = 'welcome to code jam'

with open(input_path, 'r') as input_file:
    cases = int(input_file.readline().strip())

    for i in range(1, cases + 1):

        line = input_file.readline().strip()
        dp = [0] * len(pattern)

        for c in line:

            for index in range(len(dp)):

                if pattern[index] == c:

                    dp[index] = (dp[index] + dp[
                        index - 1]) % 10000 if index > 0 else dp[index] + 1

        print('Case #%d: %04d' % (i, dp[len(dp) - 1]))
