import numpy as np


#THIS ANSWER NOT YET TESTED.

def min_change(coins, diff):
    m = [[0 for x in range(diff+1)] for x in range(len(coins) +1)]
    for i in range(diff+1):
        m[0][i] = i
    for c in range(1, len(coins)+1):
        for r in range(1, diff+1):
            if coins[c-1] == r:
                m[c][r] = 1
            elif coins[c-1] > r:
                m[c][r] = m[c-1][r]
            else:
                m[c][r] = min(m[c-1][r], 1+m[c][r-coins[c-1]])
    return m[-1][-1]

def mod_change(coins, m):
#if canonical change system greedy algorithm will work.
    coins.sort(reverse=True)
    change = []
    for c in coins: #iterate over coins in reverse order:
        n = 0
        while (n+1)*c <= m:
            n += 1
        m -= n*c
        change.append(n)
    return [x for x in reversed(change)]

def distribute_chocolate(distribution):
    operations = 0
    distribution.sort()
    coins = [1,2,5]
    operation_count = []
    #need to test three different starting places for 0th element,
    for i in range [1,2,5]:
      distribution[0] -= i
      for n in range(len(distribution)-1):
        if (distribution[n] < distribution[n+1]):
            diff = distribution[n+1] - distribution[n]
            min_changes = min_change(coins, diff)
            for i in range(len(distribution)):
                if i != n+1:
                    distribution[i] += diff
            operations += min_changes
        else:
            pass
      if len(set(distribution)) == 1: 
        operation_count.append(operations)
        break
    #return operations

def run_distribute():
  t = int(raw_input())
  for tc in range(t):
    N = int(raw_input())
    arr = map(int, raw_input().split(' '))
    print distribute_chocolate(arr)

if __name__=='__main__':
  coins = [1,5,10,25]
  m = 32
  for m in range(100):
    print mod_change(coins, m)
  #run_distribute()
