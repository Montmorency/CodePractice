class Heap(object):
  def __init__(self,a, max_heap=True):
    self.heap = a
    self.max_heap = max_heap
    self.heaped = False
    self.verbose = False

  def compare(self, x, y):
    if self.max_heap:
      if x < y: return True
      else: return False
    else:
      if x < y: return False
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
    """
    starting at initial key root, recurse
    down tree to restore heap property.
    """
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

  def up_heap(self, a, start, end):
    """
    sift heap up from end index to start index.
    """
    root = end
    while root > start:
      parent = self.parent(root)
      if self.compare(parent, a[root]):
        self.swap(a, parent, root)
        root = parent
      else:
        return

  def push(self,a,v):
    """
    Add value v to heap
    """
    a.append(v)
    self.up_heap(a, 0, N)

  def pop(self):
    a.pop(0)
    self.down_heap(a, 0, len(a))

  def heap_sort(self):
    if self.verbose: print 'Before heap', self.heap
    self.heapify(self.heap, len(self.heap))
    if self.verbose: print 'Heaped', self.heap
    a = list(self.heap)
    N = len(a)-1
    while N > 0:
      self.swap(a, 0, N)
      if self.verbose: print 'swapped', a
      N -= 1
      self.down_heap(a, 0, N)
      if self.verbose: print 'reheaped', a
    return a
      

a = [3,4,1,2,9,8,1,13,6,7]
#a = [4,3,1]#,2,9,8,1,13,6,7]
#a=[3,9,8]
heap = Heap(a, max_heap=True)
heap.verbose = True
print a
a = heap.heap_sort()
print a

