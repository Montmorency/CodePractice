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
        active_node.subnodes += 1 #incremenet root
        for lett in name:
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

    def find_contact(self, node, partial):
        total = 0
        for child in node.children:
            if child.label == partial[0]:
                if len(partial) > 1:
                  return self.find_contact(child, partial[1:])
                else:
                  return child.subnodes
        return total

    def extend_trie_recursive(self, node, name):
        node.subnodes += 1
        if name:
            if node.children:
                found_node = False
                for child in node.children:
                    if name[0] == child.label:
                        found_node=True
                        self.extend_trie(child, name[1:])
                    if not found_node:
                      new_node = Node(name[0])
                      node.children.append(new_node)
                      self.extend_trie(new_node, name[1:])
            else:
                new_node = Node(name[0])
                node.children.append(new_node)
                self.extend_trie(new_node, name[1:])     
        else: 
            return
        
    def add_contact(self,name):
        self.extend_trie(self.contacts, name)
        


def walk_tree(node):
  print node.subnodes
  print node.label
  if node.children:
    for child in node.children:
      walk_tree(child)
  else:
    return

if __name__=='__main__':
  contacts = Contacts()
  input_file = open('input.txt','r')
  g = open('output.txt','w')
  for line in input_file.read().split('\n')[:-1]:
    op, contact = line.strip().split(' ')
    if op =='add':
      contacts.add_contact(contact)
    elif op =='find':
      print len(contact)
      print >> g, contacts.find_contact(contacts.contacts, contact)
  g.close()
  #contacts.add_contact('hack')
  #contacts.add_contact('hackerrank')
  #contacts.add_contact('hasqweoiuew')
  #contacts.add_contact('hasckasdf')
  #contacts.add_contact('hbsckasdf')
  #contacts.add_contact('absdflkj')
  #contacts.add_contact('acsdflkj')
  #contacts.add_contact('esdflkj')
  #print contacts.find_contact(contacts.contacts, 'hac')
  #print contacts.find_contact(contacts.contacts, 'hak')
  #print contacts.find_contact(contacts.contacts, 'ha')
  #print contacts.find_contact(contacts.contacts, 'a')
  #print walk_tree(contacts.contacts)




