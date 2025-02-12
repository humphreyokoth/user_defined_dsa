# collections module = deque
# deque is a double-ended queue. It can be used to add or remove elements from both ends.
# deque is a part of the collections module.

import collections
stack = collections.deque()
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)

print(stack)

stack.pop()

print(stack)


# Queue module  lifoqueue

#  lifoqueue is a queue where the last element added is the first one to be removed.
#  lifoqueue is a part of the queue module.
import queue

stack = queue.LifoQueue()

stack.put(10)
stack.put(20)
stack.put(30)

stack.put(40)

stack.get()
print(stack.get())
print(stack.get())
