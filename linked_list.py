# linked list is chain of node in which each node contains data and a pointer to the next node
# Nodes are connected using pointers
# head /front is the first node of the linked list
# tail/end is the last node of the linked list which points to null

# its a dynamic data structure
# it is not stored in contiguous memory location. It is stored in random memory locations

# Advantages of linked list
# 1. Dynamic data structure
# 2. Memory utilization is efficient
# 3. Insertion and deletion of elements are easy
# 4. Size of the linked list can be changed dynamically
# 5. Implementation is easy
# 6. No need to specify the size of the linked list
# 7.can be used to implement stack queue and graph
# 8.Respresent and manipulate polynomials.  Polynomial can be represented as a linked list where each node contains the coefficient and the power of the variable in the polynomial term.

# Disadvantages of linked list
# 1. Random access is not allowed. We have to access the elements sequentially starting from the head node.
# 2. Extra memory is required for the pointer to the next node.
# 3. Reverse traversing is difficult in a singly linked list.
# 4. Memory utilization is inefficient as pointers require extra memory.


# Types of linked list
# 1. Singly linked list
# 2. Doubly linked list
# 3. Circular linked list


# singly linked list
# is a chain of data structures where each data structure contains data and a pointer to the next data structure in the chain
# head is the first node of the linked list
# tail is the last node of the linked list which points to null
# singly linked list is a linear data structure
# singly linked list is a dynamic data structure
# singly linked list is not stored in contiguous memory locations
# singly linked list is not indexed
# singly linked list is not ordered
# singly linked list is not mutable
# singly linked list is not nested
# singly linked list is not nested list
# singly linked list is not nested tuple
# singly linked list is not nested dictionary
# singly linked list is not nested set

# Operations
# 1. Insertion
# 2. Deletion
# 3. Traversing


# Adding elements to the linked list
# 1. At the beginning of the linked list
# 2. At the end of the linked list
# 3. At the middle or inbetween of the linked list

# Adding elements to the linked list
# 1.Create a node
# 2.Change new node next to head
# 3.Point head to the new node

# Add element to the end of a linked list
# 1. Create a node
# 2. Go to the last node
# 3. Change the next of the last node to the new node

# Add node inbetween two nodes
# 1. Create a node
# 2. Go to the previous node

# Deleting elements from the linked list
# 1. At the beginning of the linked list
# 2. At the end of the linked list
# 3. At the middle or inbetween of the linked list


# Traverse the linked list

# 1. Start from the head node
# 2. Traverse the linked list until we reach the last node


# singly linked list implementation
class Node:

    def __init__(self, data):
        self.data = data
        self.ref = None


""""
Travesal of the linked list
"""


class LinkedList:

    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref


LL1 = LinkedList()
LL1.print_LL()

# Adding elements at the beginning of the linked list
class Node:

    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:

    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is   empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"---->" ,end =  "")
                n = n.ref
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

# Add element at the end of the linked list
    def add_end(self,data):
        new_node  = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

# Add node inbetween two nodes in the linked list
    
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in the linked list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
#  Adding a node before
    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

# Inserting a node when linked list is completely empty

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")
        
        
# delete the first node in the linked list 
    def  delete_begin(self):
        if self.head is None:
            print("Linked list is empty cant delete nodes")
        else:
            self.head = self.head.ref

# delete the last node in the linked list

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_by_value(self, x):
        if self.head is None:
            print("Linked list is empty")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present in the linked list")
        else:
            n.ref = n.ref.ref



LL1 = LinkedList()
LL1.add_begin(10)
# LL1.add_end(100)
# LL1.add_end(200)
LL1.add_begin(20)
# LL1.add_after(30, 100)
# LL1.add_before(40, 100)
# LL1.insert_empty(10)
# LL1.insert_empty(50)
# LL1.delete_begin()
# LL1.delete_end()
LL1.delete_by_value(20)
LL1.print_LL()

