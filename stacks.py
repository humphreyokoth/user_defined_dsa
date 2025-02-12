# # stacks are implemented using lists in python  
# # stack is a collection of elements, which follows the LIFO order
# # LIFO: Last In First Out
# # stack is a linear data structure
# # stack is a collection of elements, which follows the LIFO order

# # stack operations 


# # push: add an element to the top of the stack
# # pop: remove an element from the top of the stack
# # peek: get the top element of the stack without removing it
# # is_empty: check if the stack is empty
# # size: get the number of elements in the stack
# # top: get the top element of the stack without removing it
# # clear: remove all the elements from the stack

# # push operation
# stack = []
# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(4)
# stack.append(5)
# print(stack)
# # pop operation
# stack.pop()
# print(stack)
# # peek operation
# print(stack[-1])
# # is_empty operation
# print(len(stack) == 0)
# # size operation
# print(len(stack))
# # top operation
# print(stack[-1])
# # clear operation
# stack.clear()
# print(stack)
# print(len(stack) == 0)
# # stack implementation using list
# stack = []
# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(4)
# stack.append(5)
# print(stack)
# stack.pop()
# print(stack)
# print(stack[-1])
# print(len(stack) == 0)
# print(len(stack))
# print(stack[-1])
# stack.clear()
# print(stack)
# print(len(stack) == 0)



# # implementing stacks using lists and modules 

# # push we use append
# # pop we use pop
# # peek we use [-1]
# # is_empty we use len(stack) == 0
# # size we use len(stack)
# # top we use [-1]
# # clear we use clear()

# # stack implementation using list
# stack = []
# len(stack)==0
# print(len(stack)==0)
# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.append(40)
# stack.append(50)
# print(stack)

# stack.pop()
stack  = []
def push():
    element = input("Enter the element: ")
    stack.append(element)
    print(stack)


def pop():
    if not stack:
        print("Stack is empty")
    else:
        e = stack.pop()
        print("Removed element: ", e)
        print(stack)
while True:
    print("Select the operation 1. push 2. pop 3. quit")
    choice = int(input())
    if choice ==1:
        push()
    elif choice ==2:
        pop()
    elif choice ==3:
        break
    else:
        print("Enter the correct operation")


# Stack with limit

stack = []
def push():
    if len(stack) == n:
        print("Stack is full")
    else:
        element = input("Enter the element: ")
        stack.append(element)
        print(stack)

def pop():
    if not stack:
        print("Stack is empty")
    else:
        e = stack.pop()
        print("Removed element: ", e)
        print(stack)

n = int(input("Enter the size of the stack: "))

while True:
    print("Select the operation 1. push 2. pop 3. quit")
    choice = int(input())
    if choice ==1:
        push()
    elif choice ==2:
        pop()
    elif choice ==3:
        break
    else:
        print("Enter the correct operation")


