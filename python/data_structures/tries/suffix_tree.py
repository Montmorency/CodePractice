class Node(object):
  def __init__(self, value, index=0):
    self.value = value
    self.children = []
    self.index = index

class SetSuffixTree(object):
  """
  From Skiena on Data Structures, given a reference string S 
  this is useful for finding all the places where an 
  arbitrary query string q is a substring of S.  Also
  War Story: String 'em up. The example trees generated
  are taken from the book.
  """
  def __init__(self):
    pass

  def print_children(self, children):
    """
    Accepts list of children, and prints their values.
    """
    for c in children:
      print c.value

  def construct_trie(self, trie, words): 
    chars=[]
    for word in words:
      chars.append(word[0])
    chars=list(set(chars))
    for char in chars:
      trie.children.append(Node(char))
    words_dict = {}
    for char in chars:
      words_dict[char] = []
    for key in words_dict.keys():
      for word in words:
        if word[0] == key:
          if len(word) > 1:
            words_dict[key].append(word[1:])
          else: 
            return
    self.print_children(trie.children)
    for child in trie.children:
      print words_dict[child.value]
      self.construct_trie(child, words_dict[child.value])

  def walk_tree(self, new_trie, space):
    """
    Cheap and cheerful way of printing the trees.
    """
    print space+new_trie.value
    for child in new_trie.children:
      self.walk_tree(child,space+'\t')

if __name__=='__main__':
  words = ['there', 'their', 'was', 'when']
  trie = Node('')
  suffix = SetSuffixTree()
  suffix.construct_trie(trie, words)
  suffix.walk_tree(trie,'\t')

  words = ['ACAC','CACT']
  trie = Node('')
  suffix = SetSuffixTree()
  suffix.construct_trie(trie, words)
  suffix.walk_tree(trie,'\t')
