import imp


import collections
queue = collections.deque()
queue.appendleft(10)
queue.appendleft(20)
print(queue)
queue.pop()
print(queue)

