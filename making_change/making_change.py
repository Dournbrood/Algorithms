#!/usr/bin/python

import sys


def making_change(amount, denominations, last_change=None, combinations=None):
    if last_change == None:
        last_change = float("inf")
    if combinations == None:
        combinations = 0
    if amount == 0:
        return 1

    for change_dispensed in denominations:
        if change_dispensed <= last_change:
            change_remaining = amount - change_dispensed
            if change_remaining == 0:
                return combinations + 1
            elif change_remaining > 0:
                combinations = making_change(
                    change_remaining, denominations, change_dispensed, combinations)

    return combinations


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
