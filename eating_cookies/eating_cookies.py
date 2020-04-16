#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    if cache == None:
        cache = 0
    if n == 0:
        return 1

    for num_eaten in [1, 2, 3]:
        cookies_remaining = n - num_eaten
        if cookies_remaining == 0:
            return cache + 1
        elif cookies_remaining > 0:
            cache = eating_cookies(cookies_remaining, cache)

    return cache


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
