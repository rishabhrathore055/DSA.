# dictionary is a collection of key-value pairs and the keys are unique

di = {} # empty dictionary
di = dict() # also create a dictionary like this
dict = {'a': 21, 'b': 22, 'c': 23, 'd': 24, 'e': 25}
print(dict) # {'a': 21, 'b': 22, 'c': 23, 'd': 24, 'e': 25}
print(type(dict)) # <class 'dict'>
# In dictionary we can't access the elements by index because it is not a sequence
# The keys is not in mutable type but value can be mutable
# accessing dictionary element

print(dict['a']) # 21 
# print(dict[0]) # TypeError: list indices must be integers or slices, not str
# dictinary is mutable

# nested dictionary
dict = {'a': 21, 'b': 22, 'c': {'a': 26, 'b': 27}} 
print(dict['c']) # {'a': 26, 'b': 27}
print(dict['c']['a']) # 26
