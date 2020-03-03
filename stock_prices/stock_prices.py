#!/usr/bin/python

import argparse

def find_max_profit(prices):

  current_max_profit = 0
  current_profit = 0

  for i in range(0, len(prices) - 1):
    if prices[i] < prices[i+1]:
      current_profit += prices[i+1] - prices[i]
      if current_profit > current_max_profit:
        current_max_profit = current_profit
    else:
      if current_profit > current_max_profit:
        current_max_profit = current_profit
      else:
        current_profit = 0


  return current_max_profit
  


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
