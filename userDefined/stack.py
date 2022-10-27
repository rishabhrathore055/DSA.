#stack store the elements in first out(LIFO) and First in last out(FILO) manner
# the operation of stack are push, pop, peek, isEmpty, peek or top, size

# Stack implementation
from turtle import st


stack = []
def push():
    elements = input("Enter the element: ")
    stack.append(elements)
    print(stack)
def pop_element():
    if not stack:
        print("Stack overflow")
    else :
        element = stack.pop()
        print("Removed element from",element)
        print(stack)

while True:
    print("Select the operation 1. push 2. pop 3. quit")
    choice = int(input())
    if(choice == 1):
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the valid choice: ")
    




