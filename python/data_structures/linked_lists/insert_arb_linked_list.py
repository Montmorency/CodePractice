"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    if head == None:
        return Node(data)
    if position == 0:
        new_node = Node(data)
        new_node.next = head
        return new_node
    else:
        pos = 0
        node = head
        while pos < position:
            parent = node
            node = node.next
            pos += 1
        parent.next = Node(data, node)
        return head  
