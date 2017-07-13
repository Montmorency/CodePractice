import datetime
def fib(N):
  if N <= 0: 
    return 0
  elif N == 1:
    return 1
  elif N == 2:  
    return 1
  return fib(N-1) + fib(N-2)

def fib_memo(n, fib=[]):
  for i in range(0,n):
    if i == 0:
      fib.append(0)
    elif i == 1:
      fib.append(1)
    else:
      fib.append(fib[i-2]+fib[i-1])
  return fib[n-1]+fib[n-2]

for i in range(1, 11):
  print fib(i)

for i in range(1, 11):
  print fib_memo(i, memo=[])

