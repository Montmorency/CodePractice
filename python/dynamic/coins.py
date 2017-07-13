import os
import sys

def make_change(coins, target):
  """
  Returns total number of ways that change can be made
  """
  ways = [1] + target*[0]
  for coin in coins:
    for r in range(coin, target+1):
      ways[r] += ways[r-coin]
  return ways[-1]

def min_change(coins, target):
  m_ij = [1] + [0]*target
  for coin in coins:
    for n in range(coin, target + 1):
      m_ij[n] = 1 + min([m_ij[n-c] for c in coins])
  return m_ij[-1]

if __name__ == '__main__':
  coins = [1,2,3]
  n = 4
  n = 10 
  coins = [2,5,3,6]
  res_list = []
  print make_change(coins, n)
  print min_change(coins, n)
