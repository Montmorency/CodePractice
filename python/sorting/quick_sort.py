import os
import sys

def quick_sort(sequence):
  if sequence:
    pivot = sequence[0]  
    small_list = []
    big_list = []
    if len(sequence)>1:
      for a in sequence[1:]:
        if a <= pivot:
          small_list.append(a)
        else:
          big_list.append(a)
      return quick_sort(small_list)+[pivot]+quick_sort(big_list)
    else:
      return [pivot]
  else:
    return []

if __name__=='__main__':
  sequences = [[1,4,3,25,6], ['g','b','h','z','f','g','a','e']]
  for seq in sequences:
    print 'Unsorted list', seq
    print 'Sorted list', quick_sort(seq)
