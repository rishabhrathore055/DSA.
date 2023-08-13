def getSmaller(l1,x):
    res = []
    for n in l1:
        if n < x:
            res.append(n)
    return res

print(getSmaller((list(map(int,input("Enter a list : ").split()))),int(input("Enter a target : "))))