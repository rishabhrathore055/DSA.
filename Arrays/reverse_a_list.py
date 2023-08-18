def reverse(l1):
    f = 0
    l = len(l1)-1
    while f < l:
        l1[f],l1[l] = l1[l],l1[f]
        f+=1
        l-=1
    return l1
print(reverse([1,2,2,3,4,4,5]))