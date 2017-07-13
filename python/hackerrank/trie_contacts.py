class Node(object):
    def __init__(self,label):
        self.label = label
        self.children = []
        self.subnodes = 0
        
class Contacts(object):
    def __init__(self):
        self.contacts = Node('')
    def extend_trie(self, node, name):
        active_node = node
        active_node.subnodes += 1
        for char_num, lett in enumerate(name):
            if active_node.children:
                found_node = False
                for child in active_node.children:
                    if child.label==lett:
                        active_node = child
                        found_node = True
                        active_node.subnodes += 1
                if not found_node:
                    new_node = Node(lett)
                    active_node.children.append(new_node)
                    active_node = new_node  
                    active_node.subnodes += 1
            else:
                new_node = Node(lett)
                new_node.subnodes += 1
                active_node.children.append(new_node)
                active_node = new_node
    def add_contact(self,name):
        self.extend_trie(self.contacts, name)
    def find_contact(self, node, partial):
        total = 0
        for child in node.children:
            if child.label == partial[0]:
                if len(partial) > 1:
                  return self.find_contact(child, partial[1:])
                else:
                  return child.subnodes
        return total

n = int(raw_input().strip())
contacts = Contacts()
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op =='add':
        if len(contact) < 15:
            contacts.add_contact(contact)
        else:
            contacts.add_contact(contact[:14])
    elif op =='find':
        if len(contact) < 15:
            print contacts.find_contact(contacts.contacts, contact)
        else:
            print contacts.find_contact(contacts.contacts, contact[:14])


