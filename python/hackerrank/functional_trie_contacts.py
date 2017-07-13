class Contacts(object):
    def __init__(self):
        self.contacts=[]
    
    def add_contact(self,name):
        self.contacts.append(name)
    
    def find_contact(self, partial):
        small_list = filter(lambda x: x[:len(partial)] == partial, self.contacts)
        return len(small_list)

n = int(raw_input().strip())
contacts = Contacts()
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op =='add':
        contacts.add_contact(contact)
    elif op =='find':
        print contacts.find_contact(contact)
    else:
        pass
