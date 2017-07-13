"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    tmp = head
    visited_nodes=[]
    while tmp.next != None:  
        if tmp.data not in visited_nodes:
            visited_nodes.append(tmp.data)
            tmp = tmp.next
        else:
            return True
    return False
