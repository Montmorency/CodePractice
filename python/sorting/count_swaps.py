import random
from collections import deque
def merge(a, b):
    result = []
    swaps = 0 
    a = deque(a)
    b = deque(b)
    while a and b:    
        if a[0] <= b[0]:
            result.append(a.popleft())
        elif a[0] > b[0]:
            swaps += len(a)
            result.append(b.popleft())
    while a:
        result.append(a.popleft())
    while b:
        result.append(b.popleft())
    return result, swaps

def merge_sort(a):
    if len(a) > 1:
        left = a[:len(a)/2]
        right = a[(len(a)/2):]
        left_sort, swaps_l  = merge_sort(left)
        right_sort, swaps_r  = merge_sort(right)
        result, swaps = merge(left_sort, right_sort)
        return result, swaps + swaps_l + swaps_r
    else:
        return a, 0 
    
def count_inversions(a):
    a, swaps = merge_sort(a)
    return a, swaps

#t = int(raw_input().strip())
t =1
arr = [2,1,3,1,2]
arr = [1,1,1,2,2]
with open('input_1.txt','r') as f :
  arrs = f.read().split('\n')
print len(arrs)
for a in arrs[:-1]:
  a = map(int, a.split(' '))
  #print count_inversions(a)
  #a = [random.randint(1,100) for i in range(20)]
  with open('array.txt','w') as g:
    a, swaps = count_inversions(a)
    print swaps
    print >> g, a
