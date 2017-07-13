import os
import sys

def bubble_sort(sequence):
  not_sorted = True
  i = 0
  while not_sorted:
    a = sequence[i]
    b = sequence[i+1]
    if a > b:
      sequence[i] = b
      sequence[i+1] = a
      not_sorted = True
      i = 0
    elif (a <= b) and i < (len(sequence)-2):
      i += 1
    else:
      not_sorted = False
  return sequence

if __name__=='__main__':
  sequences = [[1,4,3,25,6], ['g','b','h','z','f','g','a','e']]
  for seq in sequences:
    print 'Unsorted list', seq
    print 'Sorted list', bubble_sort(seq)
