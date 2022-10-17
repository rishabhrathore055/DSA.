# the difference between tuples and lists is that tuples are immutable and lists are mutable
tup = (1,33.4,'hello',True)
print(tup)
print(type(tup)) #Cheking the type of the variable

tup1 = tuple() # creating empty tuple
tup1 = (2,4,6,8)
print(tup1) # ()
# in tuple we can't add or delete the elements beacuse it is immutable
# accessing tuple element
print(tup1[0]) # 2

# nested tuple
tup2 = (1,2,3,(4,5,6))
print(tup2[3]) # (4, 5, 6)