class Node(object):
    def __init__(self, price):
        self.id_ = 0
        self.price = price
        self.right_child = None
        self.left_child = None


def build_tree(seq):
  if len(seq) == 0:
    return None
  med = len(seq)//2
  left = seq[:med]
  right = seq[med+1:]
  node = Node(seq[med])
  node.left_child = build_tree(left)
  node.right_child = build_tree(right)
  return node

if __name__=='__main__':
  a = [1,4,5,3,2]
  root = build_tree(a)
  print root.price
  
