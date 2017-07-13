from datetime import datetime
class Node(object):
    def __init__(self, id_, price):
        self.id_ = id_
        self.price = price
        self.right_child = None
        self.left_child = None

    def __repr__(self):
      return 'Node id price '+' '.join(map(str,[self.id_, self.price]))
        
class IceCream(object):
    def __init__(self, money, prices, id_to_price):
        self.money = money
        self.prices = prices
        self.id_to_price = id_to_price
        self.solution = []
        self.solved = False
        self.nodes = []
        #self.root = self._add_keys()
        #self.root = self.build_tree(sorted(self.id_to_price.items(), key=lambda x:x[1]))
        self.root = self.build_tree(self.id_to_price.items())
        self.first_choice = 0
             
    def build_tree(self, seq):        
        """
        Only works without duplicates.
        """
        if len(seq) == 0:
          return None
        med = len(seq)/2
        left = seq[:med]
        right = seq[med+1:]
        node = Node(seq[med][0], seq[med][1])
        self.nodes.append(node)
        node.left_child = self.build_tree(left)
        node.right_child = self.build_tree(right)
        return node

    def _add_keys(self):
      first = True
      tmp_items = self.id_to_price.items()
      for k, v in self.id_to_price.items():
        if not first:
          self._insert(root, k, v)
        else:
          root = Node(k, v)
          self.nodes.append(root)
          first = False
      return root
   
    def _insert(self, node, k, v):
      if a <= node.price:
        if node.left_child:
          self._insert(node.left_child, k, v)
        else:
          child = Node(k, v)
          node.left_child = child
          self.nodes.append(child)
      else:
        if node.right_child:
          self._insert(node.right_child, k, v)
        else:
          child  = Node(k,v)
          node.right_child = child
          self.nodes.append(child)

    def find_solution(self, node, money):
        if (money == node.price) and (node.id_ != self.first_choice):
            self.solution.append(node)
            self.solved = True
        if node.right_child and (not self.solved):
            self.find_solution(node.right_child, money)
        if node.left_child and (not self.solved):
            self.find_solution(node.left_child, money)
            
    def gen_solution(self):
        for node in self.nodes:
            self.first_choice = node.id_
            self.solution.append(node)
            node.right_child
            if node.price <= self.money: #only start with ice creams less than total money
              money = self.money - node.price
              self.find_solution(self.root, money)
            if self.solved:
              break
            else:
              self.solution.pop()
                                                             
    def print_solution(self):
        self.solution.sort(key=lambda x:x.id_)
        print self.solution[0].id_, self.solution[1].id_

    def _print_nodes(self, node):
      print 'PN', node
      if node.left_child:
        self._print_nodes(node.left_child)
      if node.right_child:
        self._print_nodes(node.right_child)

    def print_nodes(self):
      self._print_nodes(self.root)

if __name__ == '__main__':
  #with open('input.txt','r') as f:
  with open('ice_input_3.txt','r') as f:
    data = f.read().split('\n')
  data_sets = int(data[0])
  m = 3
  time1 = datetime.now()
  for chunk in [data[m*i:m*i+m] for i in range(len(data)/3)]:
    m = int(chunk[0])
    n = int(chunk[1])
    a = map(int, chunk[2].split(' '))
    #print m,n,a
    id_to_price = {}
    for k, v in enumerate(a):
      id_to_price[k+1] = v 
    trip = IceCream(m, a, id_to_price)
    trip.gen_solution()
    #trip.print_nodes()
    trip.print_solution()                                             
  delta = datetime.now() - time1
  print 'micro', delta.microseconds
