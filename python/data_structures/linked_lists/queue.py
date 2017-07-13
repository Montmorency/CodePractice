class DeQueue(object):    
    def __init__(self):
        from collections import deque
        self.first = deque()
        self.second = deque()
    
    def peek(self):
        return self.first[0]
                
    def pop(self):
        self.first.popleft()
        
    def put(self, value):
        self.first.append(value)

class DualQueue(object):
  def __init__(self):
    self.first = []
    self.second = []

  def flip_second():
    while self.second:
      self.first.append(self.second.pop())

  def peek(self):
    if not self.first:
      self.flip_second()
    return self.first[-1]

  def pop(self):
    if not self.first:
      self.flip_second()
    self.first.pop()

  def push(self, value):
    self.second.append(value)

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())   
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
