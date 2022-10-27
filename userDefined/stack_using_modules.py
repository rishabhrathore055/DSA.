# in collection module there a a class called deque we use it as a stack 
# deque stands for double ended queue 
import collections 
# using collections deque class
# stack = collections.deque()
# stack.append(10)  # append used for pusing the elements in the array
# stack.append(20)
# stack.append(30)
# stack.append(40)
# stack.append(50)
# stack.pop()
# stack.pop()
# print(not stack) # check if the stack is empty or not

# using queue
import queue
stack = queue.LifoQueue(3)
stack.put(10) # put used for pusing the elements in the stack
stack.put(20)
stack.put(30)
stack.put(40,timeout=1)
stack.get() # get used for poping the elements in the stack
print(stack)
print(not stack) # check if the stack is empty or not


print(stack)