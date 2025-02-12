# Priority  Queue  implementation  
#  Modified versions of queues

#  list 
# Priority Queue is an extension of the queue with following properties.


q = []
q.append(10)
q.append(40)
q.append(20)
q.append(30)
q.sort()
print(q)

q.pop()

print(q)


import queue
q= queue.PriorityQueue()
q.put(10)   
q.put(60)
q.put(30)
q.put(20)
q.put(40)
print(q)
q.get()
print(q)
q.get()
print(q)

q.append((1,"alexa "))
q.append((4,"alex"))

q.append((2, "al"))
q.sort(reverse=True)

print(q)