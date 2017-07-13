from datetime import datetime
from collections import deque



avg_time = 0
N = 10000
for i in range(N):
  a = [i for i in range(4000)]
  time1 = datetime.now()
  del a[0]
  delta = datetime.now()-time1
  avg_time += delta.microseconds
print avg_time/float(N)
print 'del a[0] Avg Time {} runs'.format(N), avg_time/float(N)

avg_time = 0
for i in range(N):
  a = [i for i in range(4000)]
  time1 = datetime.now()
  a.pop(0)
  delta = datetime.now()-time1
  avg_time += delta.microseconds
print 'a.pop(0) Avg Time {} runs'.format(N), avg_time/float(N)


avg_time = 0
for i in range(N):
  a = [i for i in range(4000)]
  time1 = datetime.now()
  a = a[1:]
  delta = datetime.now()-time1
  avg_time += delta.microseconds
print avg_time/float(N)
print 'a[1:] Avg Time {} runs'.format(N), avg_time/float(N)

avg_time = 0
for i in range(N):
  a = deque()
  [a.append(i) for i in range(4000)]
  time1 = datetime.now()
  a.popleft()
  delta = datetime.now()-time1
  avg_time += delta.microseconds
print avg_time/float(N)
print 'deque(0) a.pop left Avg Time {} runs'.format(N), avg_time/float(N)
