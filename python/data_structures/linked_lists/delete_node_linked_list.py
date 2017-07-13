"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    if head == None:
        return None   
    if position==0:
        if not head.next:
            return None
        else:
            return head.next
    else:
        pos = 0
        parent = head
        node = head.next
        while pos < position:           
            if pos != 0:
                parent = parent.next           
            node = node.next
            pos += 1       
        parent.next = node
        return head
