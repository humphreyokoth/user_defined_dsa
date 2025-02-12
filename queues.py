# queue is data structure where the first element added is the first one to be removed
# queue works with fifo order (first in first out)
# queue is a part of the queue module
# queue is a linear data structure where the elements are added at the end and removed from the front
# queue where the first element added is called back /rear/tail and the last element added is called front/head
# LILO methodology that is last in last out


# enqueue: add an element to the end of the queue
# dequeue: remove an element from the front of the queue
# isFull: check if the queue is full
# isEmpty: check if the queue is empty

#  Used whe you want things one at atime in the order they were added

# Implementations
# 1. Using list

# enqueue append method
# dequeue pop method

# queue = []
# queue.append(10)
# queue.append(20)
# queue.append(30)
# queue.append(40)
# print(queue)

# # removing the first element
# queue.pop(0)
# print(queue)


# # inserting at the front
# queue.insert(0, 50) 
# queue.insert(0, 60)
# queue.insert(0, 70)

# print(queue)

queue = []
def enqueue():
    element = input("Enter the element: ")
    queue.append(element)
    print(element, "is added to the queue")  

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        e = queue.pop(0)
        print("Element removed: ", e)

def display():
    print(queue)

while True:
    print("Select the operation 1. add 2. remove 3. show 4. quit")
    choice = int(input())
    if choice ==1:
        enqueue()
    elif choice ==2:
        dequeue()
    elif choice ==3:
        display()
    elif choice ==4:
        break
    else:
        print("Enter the correct operation")    
    

# 2. Using collections 
# deque is a double-ended queue. It can be used to add or remove elements from both ends.
# deque is a part of the collections module.

import collections
q = collections.deque()

print(q)
# adding elements to the queue
q.appendleft(10)

q.appendleft(20)

q.appendleft(30)

print(q)
# removing the first element
q.pop()
print(q)

q.pop()

print(q)

# adding elements to the queue
q.append(10)

q.append(20)
q.append(30)
print(q)

# removing the first element
q.popleft()
print(q)


# 3. Using queue module
# queue is a linear data structure where the elements are added at the end and removed from the front
# queue where the first element added is called back /rear/tail and the last element added is called front/head
# LILO methodology that is last in last out

import queue

q = queue.Queue()

q.put(10)

q.put(20)

q.put(30)

print(q)
# removing the first element
q.get()
print(q)
q.get()

print(q)



#  queue class 


q= queue.Queue()
q.put(10)
q.put(20)
q.put(30)
q.put(40)
print(q)
q.get()
print(q)
q.get()
print(q)

