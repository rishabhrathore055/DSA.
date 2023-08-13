l1 = [x for x in range(1,11) if x%2==0]
print(l1)

l2 = [x for x in range(11) if x%2!=0]
print(l2)

def getSmaller(l,x):
    return [n for n in l if n<x]
# print(getSmaller((list(map(int,input("Enter a list : ").split()))),int(input("Enter a target : "))))

def seprator(l):
    Even =[x for x in l if x%2==0]
    Odd = [x for x in l if x%2!=0]
    return Even,Odd
# print(seprator((list(map(int,input("Enter a list : ").split())))))



s = "geeksforgeeks"
l1 = [x for x in s if x in "aeiou"]
print(l1)


# Square
print([i**2 for i in range(6)])