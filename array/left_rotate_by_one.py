def rotateByone(l1):
    n = len(l1)
    x = l1[0]
    for i in range(1,n):
        l1[i-1] = l1[i]
    l1[n-1] = x
    return l1

print(rotateByone([10,20,30]))