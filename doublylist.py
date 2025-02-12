class Node:
    def __init__(self,data):
         self.data = data
         self.nref = None
         self.pref = None


class doublyLL:
    def __init__(self):
        self.head = None

# Traversal of the linked list 
    def print_LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "---->", end = "")
                n = n.nref
    
# Traversal of the linked list in reverse order
    def print_LL_reverse(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "---->", end = "")
                n = n.pref

# Insert  when empty
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")

# Add element at the beginning of the  doubly linked list

    def add_begin(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

# add elemen at the end of the doubly linked list

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node

dl1 =   doublyLL()
dl1.print_LL()
dl1.print_LL_reverse()
# Doubely linked list  is a type of linked list in which each node apart from storing its data has two links. The first link points to the previous node in the linked list and the second link points to the next node in the linked list. The first node of the linked list has its previous link pointing to null similarly the last node of the linked list has its next link pointing to null.

