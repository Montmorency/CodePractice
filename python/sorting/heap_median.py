#from collections import deque
import sys
import datetime

class Heap(object):
  def __init__(self, max_heap=True):
    self.max_heap = max_heap
    self.size = 0
    self.heap = []

  def compare(self,a,b):
    if self.max_heap: 
      return b > a
    else:
      return b < a

  def swap(self, index_a, index_b):
    self.heap[index_a], self.heap[index_b] = self.heap[index_b], self.heap[index_a]

  def parent(self,i):
    return int(float(i-1)/2.)

  def child_left(self,i):
    return int(float(2*i+1))

  def child_right(self,i):
    return int(float(2*i+2))

  def pop(self):
    root = self.heap[0]
    self.swap(0, -1)
    self.heap.pop()
    self.size -= 1
    self.down_heapify(0)
    return root

  def insert(self, a):
    self.heap.append(a)
    self.size += 1
    self.up_heapify(len(self.heap))

  def down_heapify(self, root):
    left_child = 2*root + 1
    right_child = 2*root + 2
    large_index = root
    if (right_child < len(self.heap)):
      if self.compare(self.heap[root], self.heap[right_child]): 
        large_index = right_child
    if (left_child < len(self.heap)):
      if self.compare(self.heap[large_index], self.heap[left_child]): 
        large_index = left_child
    if large_index != root:
      self.swap(root, large_index)
      self.down_heapify(large_index)

  def up_heapify(self, root):
    parent = self.parent(root)
    if root == len(self.heap):
      root = len(self.heap) - 1
    if (parent >= -1) and self.compare(self.heap[parent], self.heap[root]):
    	self.swap(parent, root)
    	self.up_heapify(parent)

def median(big_heap, small_heap, m, a):
  if big_heap.size == small_heap.size:
    if a > m:
      big_heap.insert(a)
      return float(big_heap.heap[0])
    if a <= m:
      small_heap.insert(a)
      return float(small_heap.heap[0])
  elif big_heap.size > small_heap.size:
    if a > m:
      swap = big_heap.pop()
      small_heap.insert(swap)
      big_heap.insert(a)
      return float(big_heap.heap[0] + small_heap.heap[0])/2.0
    else:
      small_heap.insert(a)
      return float(big_heap.heap[0] + small_heap.heap[0])/2.0
  elif big_heap.size < small_heap.size:
    if a < m:
      swap = small_heap.pop()
      big_heap.insert(swap)
      small_heap.insert(a)
      return float(big_heap.heap[0] + small_heap.heap[0])/2.0
    else:
      big_heap.insert(a)
      return float(big_heap.heap[0] + small_heap.heap[0])/2.0

if __name__=='__main__':
  big_heap = Heap(max_heap=False)
  small_heap = Heap(max_heap=True)
  input_data = open(sys.argv[1],'r').read().split('\n')
  g = open('output.txt','w')
  start = datetime.datetime.now()
  for i, a in enumerate(input_data[:-1]):
    a = float(a)
    if not(big_heap.size == 0 and small_heap.size == 0):
      m = median(big_heap, small_heap, m, a)
      print >> g,  m
    else:
      small_heap.insert(a)
      m = float(a)
      print >> g, m
  finish = datetime.datetime.now()
  delta = finish - start
  print 'Time:', delta.microseconds
