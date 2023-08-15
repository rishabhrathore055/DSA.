def isSorted(l1):
    if len(l1) == 0 or len(l1)==1:
        return True
    for i in range(1,len(l1)):
        if l1[i]< l1[i-1]:
            return False
    return True
print(isSorted([10,2,20,30]))