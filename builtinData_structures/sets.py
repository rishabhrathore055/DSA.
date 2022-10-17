# sets are the collection of unique elements
sets = {} #create an empty set
sets = set() # create an empty set using set() constructor

names = set(['python','java','c','c++','c#','python']) # the duplicate element will be removed
print(names) # {'c', 'java', 'c#', 'c++', 'python'}

# add element to set
names.add('ruby')
print(names)

# delete element from set
setr = {'c', 'java', 'c#', 'c++', 'python'}
setr.remove('c')
print(setr)
setr = {'c', 'java', 'c#', 'c++'} 
print('c' in setr) # True
# set can't be nested and set in unordered like dictionary be can't be accessed by index