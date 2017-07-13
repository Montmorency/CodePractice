import numpy as np
def count_ways_naive(s):
  count = 0
  if s <= 0:
    count += 0
  elif s == 1:
    count += 1
  elif s == 2:
    count += 2 
  elif s == 3:
    count += 4
  else:
    count += count_ways_naive(s-1)
    count += count_ways_naive(s-2)
    count += count_ways_naive(s-3)
  return count

def count_ways(s):
  #f_n = np.zeros(s+1, dtype=int)
  f_n =[0 for i in range(s+1)]
  for i in range(0, s+1):
    if i == 0:
      f_n[0] = 0
    elif i == 1:
      f_n[1] = 1
    elif i == 2:
      f_n[2] = 2
    elif i == 3:
      f_n[3] = 4
    else:
      f_n[i] = f_n[i-3] + f_n[i-2] + f_n[i-1]
  return f_n[-1]
    

print count_ways_naive(7)
print count_ways(7)
