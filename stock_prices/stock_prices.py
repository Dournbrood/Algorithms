#!/usr/bin/python

import argparse


def find_max_profit(prices):
    if len(prices) <= 1:
        return 0
    elif len(prices) == 2:
        return prices[1] - prices[0]
    max_profit = None

    i = 0
    k = 1

    while i in range(len(prices) - 1):
        while k in range(len(prices)):
            if max_profit == None:
                max_profit = prices[k] - prices[i]
                k += 1
            elif (prices[k] - prices[i]) > max_profit:
                max_profit = prices[k] - prices[i]
                k += 1
            else:
                k += 1
        i += 1
        k = i + 1

    return max_profit


print(find_max_profit([1050, 270, 1540, 3800, 2]))  # 3530
print(find_max_profit([540, 200, 30]))  # -170
print(find_max_profit([540, 200, 400, 440, 320, 150, 30]))  # 240
print(find_max_profit([20, 40]))  # -20
print(find_max_profit([800, 40]))  # 760
print(find_max_profit([15]))  # 0
print(find_max_profit([]))  # 0


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
