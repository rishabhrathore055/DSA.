# Queue follow the First in first out(FIFO) and last in last out(LILO) principle
# the process of adding element in the queue is enqueue
# the process of adding element in the queue is enqueue 

# operation of queue is enque and deque,isFull,isEmpty

#Implementation of queue using list 
# first way
from secrets import choice
queue = []
queue.append(10)
queue.append(20)
queue.append(30)
queue.pop(0)
queue.pop(0)
print(queue)

# second way
# queue = []
# queue.insert(0, 10)
# queue.insert(0, 20)
# queue.insert(0, 30)
# queue.pop()
# queue.pop()
# print(queue)

# implementation
queue = []
def enqueue():
    element = int(input("Enter the element: "))
    queue.append(element)
    print(element," is added to queue!")
def dequeue():
    if not queue:
        print("Queue is empty!")
    else:
        element = queue.pop(0)
        print(element," is removed from queue!")
def display():
    print(queue)


while(True):
    print("Select the operation 1. add 2. remove 3. display 4. quit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Enter the vaild choice: ")