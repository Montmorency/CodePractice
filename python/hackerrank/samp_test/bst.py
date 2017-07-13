class Node(object):
  def __init__(self, v):
    self.value = v
    self.right_child = None
    self.left_child = None

def insert_key(root, k):
  if k > root.value:
    if root.right_child:
      insert_key(root.right_child, k) 
    else:
      root.right_child = Node(k)
  if k <= root.value:
    if root.left_child:
      insert_key(root.left_child, k)
    else:
      root.left_child = Node(k)

def find_key(root,k):
  if k == root.value:
    return True
  elif k > root.value:
    if root.right_child:
      return find_key(root.right_child, k)
    else:
      return False
  elif k <= root.value:
    if root.left_child:
      return find_key(root.left_child, k)
    else:
      return False

def build_tree(root,arr):
  for a in arr:
    insert_key(root,a)

def findNumber(arr,k):
  root = Node(arr[0])
  build_tree(root, arr[1:])
  res = find_key(root, k)
  return res

arr=[3,5,6,7,8]
print findNumber(arr,8)
arr=[3,5,6,7,8]
print findNumber(arr,9)
print findNumber(arr,21)
print findNumber(arr,3)

