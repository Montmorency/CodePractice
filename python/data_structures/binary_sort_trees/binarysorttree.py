class Node(object):
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None

  def min_value(self,node):
    if node.left == None:
      return node.data
    else:
      self.min_value(node.left)

  def max_value(self, node):
    if node.right==None:
      return node.data
    else:
      self.max_value(node.right)

  def key_in_tree(self, node, key):
    if key > node.data:
      if node.right:
        return key_in_tree(node.right, key)
      else:
        return False
    elif key < node.data:
      if node.left:
        return key_in_tree(node.left, key)
      else:
        return False
    elif key == node.data:
      return True
  
  def add_key(self, node, key):
    if self.key_in_tree(node,key):
      raise Exception('Key In Tree!')
    if key > node.data:
      if node.right:
        self.add_key(node.right, key)
      else:
        node.right = Node(key)
    elif key < node.data:
      if node.left:
        self.add_key(node.left, key)
      else:
        node.left = Node(key)

  def delete_key(self, root, key):
    not_found = true 
    parent_node = root
    child_node = root
    not_found = True
    #find node to delete
    while not_found:
      if key > child_node.data:
        parent_node = child_node
        child_node = node.right
      elif key < node.data:
        parent_node = child_node
        child_node = node.left
      elif key == child_node.data:
        not_found = False
    #if leaf node deletion is trivial:
    if (not child_node.right) and (not child_node.left):
      if parent_node.data > child_node.data:
        parent_node.left = None
      elif parent_node.data < child_node.data:
        parent_node.right = None
    #if deletion node has only the one child:
    elif bool(child_node.left) ^ bool(child_node.right):
      if child_node.data > parent_node.data:
        if child_node.left:
          parent_node.right_child = child_node.left
        else:
          parent_node.right_child = child_node.right
      elif child_node.data < parent_node.data:
        if child_node.left:
          parent_node.left_child = child_node.left
        else:
          parent_node.left_child = child_node.right
    else:
          swap_value = self.find_min(child_node.right)
          child_node.value = swap_value
          self.remove(child_node.right, swap_value)
      
class BSTree(object):
  def __init__(self):
    root = None
  def add(self, value):
    if self.root = None:
      root = Node(value)
    else:
      root.add(value)
  def remove(self,value):
    if root == None:
      return False
    elif root.data == value:
      swap_value = self.find_min(root.right_child)
      root.data = swap_value 
