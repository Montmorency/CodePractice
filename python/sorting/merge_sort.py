import os
import sys
import random 

def merge_sort(a):
  def merge(left, right):
    result = []
    while left and right:
        elem_l = left[0]
        elem_r = right[0]
        if elem_l <= elem_r:
          result.append(elem_l)
          left = left[1:] #consume left
        else:
          result.append(elem_r)
          right = right[1:] #consume right
    if left:
      print 'left', left
      result = result + left
    if right:
      print 'right', right
      result = result + right
    return result

  if len(a) == 1:
    return a
  else:
    mid_point = int(float(len(a))/2.)
    left = a[:mid_point]
    right = a[mid_point:]
  return merge(merge_sort(left), merge_sort(right))

if __name__=='__main__':
  for i in range(3):
    a = [random.randint(1,100) for i in range(20)]
    print a
    print merge_sort(a)
