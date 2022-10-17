serialNum = [1, 2, 3, 4, 5]
items = [1,2.3,'hello',True] # list can contains different data types and it maintain the same order
print(serialNum)
print(items)

# accessing list elements
print(serialNum[0]) # 1
print(serialNum[-1]) # last element 5

# slicing
print(serialNum[0:3]) # [1, 2, 3]

# updating list
serialNum[0] = 10 # replace index 1 element with 10
print(serialNum) # [10, 2, 3, 4, 5]

# adding list elements
serialNum.append(6) # add 6 at the end of the list
print(serialNum) 
# deleting list elements
del serialNum[0] # delete index 0 element
print(serialNum) # [2, 3, 4, 5]

# nested list
nestedList = [1,2,3,[4,5,6]]
print(nestedList)

# list is mutable that means we can change the list elements
# List are Dynamic that means we can add or delete the list elements at any time