class Node(object):
    def __init__(self, price, id_):
        self.id_ = id_
        self.price = price
        self.right_child = None
        self.left_child = None

class IceCream(object):
    def __init__(self, money, prices, id_to_price):
        self.money = money
        self.prices = prices
        self.id_to_price = id_to_price
        self.solution = []
        self.solved = False
        self.nodes = []
        self.root = self._add_keys()
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
        node = Node(seq[med])
        self.nodes.append(node)
        node.left_child = self.build_tree(left)
        node.right_child = self.build_tree(right)
        return node

    def _add_keys(self):
        first = True
        for k,v in self.id_to_price.items():
            if not first:
                self._insert(root, k, v)
            else:
                root = Node(v,k)
                self.nodes.append(root)
                first = False
        return root

    def _insert(self, node, k, a):
        if a <= node.price:
            if node.left_child:
                self._insert(node.left_child, k, a)
            else:
                node = Node(a, k)
                node.left_child = node
                self.nodes.append(node)
        else:
            if node.right_child:
                self._insert(node.right_child,k,a)
            else:
                node = Node(a,k)
                node.right_child = node
                self.nodes.append(node)
                
    def find_solution(self, node, money):
        if (money == node.price) and (node.id_ != self.first_choice):
            self.solution.append(node)
            self.solved = True
        if node.right_child and (not self.solved) and (money > node.price):
            self.find_solution(node.right_child, money)
        if node.left_child and (not self.solved) and (money <= node.price):
            self.find_solution(node.left_child, money)

    def gen_solution(self):
        for node in self.nodes:
            self.first_choice = node.id_
            self.solution.append(node)
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

t = int(raw_input().strip())
for a0 in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    id_to_price = {}
    for k, v in enumerate(a):
        id_to_price[k+1]=v
    trip = IceCream(m, a, id_to_price)
    trip.gen_solution()     
    trip.print_solution()                                                         
