from suffix_tree import SetSuffixTree

def gen_suffix_dict(suffices):
  suff_dict = {}
  for s in suffices:
    suff_dict[s[0]] = []
  for s in suffices:
    suff_dict[s[0]].append(s)
  return suff_dict

class Node(object):
  def __init__(self, label):
    self.label = label
    self.children = []
    self.edges = []

  def __repr__(self):
    return self.label

class Edge(object):
  def __init__(self, label, to_index, from_index):
   #refers to original string.
    self.from_index = from_index
    self.to_index = to_index
    self.label = label

  def __repr__(self):
    return self.label

class ActivePoint(object):
  def __init__(self, root, edge, position):
    self.node = root 
    self.edge = edge 
    self.position = position
  def __repr__(self):
    return ' '.join(map(str, [self.node.label, self.edge.label, self.position]))

class NaiveSuffix(object):
  def __init__(self, explicit=True):
    self.explicit = explicit
    self.root = Node('')

  def check_unique(self, root, lett):
    unique = True
    for edge in root.edges:
      if lett == edge.label[0]:
        return False
    return unique

  def find_edge(self, node, lett, start, end):
    for edge in node.edges:
      if lett == edge.label[1]:
        return edge

  def gen_trie(self):
    marker = 0
    for i, lett in enumerate(string[marker:]): #phase
      for j in range(marker+1):  #extension
        if self.edges:
          check_unique(root.edges)
        else:
          root.edges.append(Edge(lett,j,i))
        for edge in root.edges:
          edge += lett
      marker += 1

class SuffixTree(object):
  """
  Following explanation on StackOverFlow:
  https://stackoverflow.com/questions/9452701/ukkonens-suffix-tree-algorithm-in-plain-english
  visualization here: http://brenden.github.io/ukkonen-animation/
  This 'suffix tree works whenever there are no repeated characters. This is a 
  trivial case.
  """
  def __init__(self, explicit=True):
    self.explicit = explicit
    self.nodes = []
    self.edges = []

  def check_unique_prefix(self, lett):
    unique = True
    for edge in self.edges:
      if lett == edge.label[0]:
        return (False, edge)
    return(unique, Edge('',-1,-1)) #return a dummy

  def index_match(self, edge, lett):
    print 'label', edge.label
    for i, char in enumerate(edge.label):
      if char == lett:
        return i 
  def gen_trie(self, root, string):
    """ Ukkonen's Algorithm """
    from collections import deque
    split_strings = deque()
    marker = 0
    remainder = 0
    root =  Node('/')
    self.nodes.append(root) #initialize root node
    active_point = ActivePoint(root, None, 0)
    active_str = ''
    for i, lett in enumerate(string[marker:]): #phases
      unique, split_edge = self.check_unique_prefix(lett)
      print active_point.edge
      active_point.edge = split_edge
      if unique:
        self.edges.append(Edge('', marker, 0))
        active_point.node.edges.append(Edge('', marker, 0))
      else:
        position = self.index_match(active_point.edge, lett)
        active_point.position = position
        print ' Active POint', active_point
        remainder +=  1
        active_str += lett
      for edge in self.edges:
        edge.label += lett
        edge.to_index = marker
      marker += 1

  def print_tree(self):
    for edge in self.edges:
      print edge.from_index, edge.to_index, edge.label

if __name__=='__main__':
#  string = 'abc'
  trie = Node('')
#  simpsuff = SimpleSuffix()
#  simpsuff.gen_trie(trie, string)
#  simpsuff.print_tree(trie)
  string = 'abcabxabcd'
  suff = SuffixTree()
  suff.gen_trie(trie, string)
  suff.print_tree()
