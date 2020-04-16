#!/usr/bin/python

import sys


# given n = 2, your function should output the following:
# [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]


# n = 1
# ________________
# 0 1
# 1 2
# 2 3


# n = 2
# ________________
# 00 11
# 01 12
# 02 13
# 10 21
# 11 22
# 12 23
# 20 31
# 21 32
# 22 33

# n = 3
# ________________
# 000 111
# 010 121
# 020 131
# 001 112
# 011 122
# 021 132
# 002 113
# 012 123
# 022 133
# 100 211
# 110 221
# 101 212
# 102 213
# 111 222
# 112 223
# 120 231
# 121 232
# 122 233
# 200 311
# 201 312
# 202 313
# 210 321
# 211 322
# 212 323
# 220 331
# 221 332
# 222 333


# The number of final pairs we get is proportional to 3 ** n

# Recursion 0, we will receive arr=[
# []
# ]

# Recursion 1, we should receive arr=[
# ['rock'],
# ['paper'],
# ['scissors']
# ]

# Recursion 2, we should receive arr=[
# ['rock', 'rock'],
# ['rock', 'paper'],
# ['rock', 'scissors'],
# ['paper', 'rock'],
# ['paper', 'paper'],
# ['paper', 'scissors'],
# ['scissors', 'rock'],
# ['scissors', 'paper'],
# ['scissors', 'scissors']
# ]


def rps_helper(n, result, arr=[]):
    # Base case
    if n <= 0:
        result.append(arr)
        return
    else:
        for play in ["rock", "paper", "scissors"]:
            rps_helper(n - 1, result, arr + [play])


def rock_paper_scissors(n):
    result = []
    rps_helper(n, result, [])
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
