class Heap(object):
  def __init__(self,a, max_heap=True):
    self.heap = a
    self.max_heap = max_heap
    self.heaped = False

  def compare(self, x, y):
    if self.max_heap:
      if x < y: return True
      else: return False
    else:
      if x <> y: return False
      else: return True

  def swap(self,a,x,y):
    #swap array value at indices x,y
    a[x], a[y] = a[y], a[x]

  def parent(self, x):
    return int((x-1)/2)

  def left_child(self,x):
    return int(2*x+1)

  def right_child(self,x):
    return int(2*x+2)

  def heapify(self, a, N):
    #build heap down from root i
    parent = self.parent(N)
    start = parent
    left_child = self.left_child(parent)
    right_child = self.right_child(parent) 
    while start >= 0:
      self.down_heap(a, start, N-1)
      start -= 1

  def down_heap(self, a, root, end):
    print 'Down heaping', a
    swap_index = root
    left_child = self.left_child(root)
    right_child = self.right_child(root)
    if (left_child <= end) and self.compare(a[swap_index], a[left_child]):
      swap_index = left_child
    if (right_child <= end) and self.compare(a[swap_index], a[right_child]):
      swap_index = right_child
    if root != swap_index: #fix everything below after swap
      self.swap(a, swap_index, root)
      self.down_heap(a, swap_index, end)

  def heap_sort(self):
    print 'Before heap', self.heap
    self.heapify(self.heap, len(self.heap))
    print 'Heaped', self.heap
    a = list(self.heap)
    N = len(a)-1
    while N > 0:
      self.swap(a, 0, N)
      print 'swapped', a
      N -= 1
      self.down_heap(a, 0, N)
      print 'reheaped', a
    return a
      

a = [3,4,1,2,9,8,1,13,6,7]
#a = [4,3,1]#,2,9,8,1,13,6,7]
#a=[3,9,8]
heap = Heap(a)
print a
a = heap.heap_sort()
print a

