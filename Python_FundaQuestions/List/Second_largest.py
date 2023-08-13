def sec_large(l):
    if len(l) <=1:
        return None
    max1 = 0
    for n in l:
        if n > max1: max1 = n
    max2 = None
    for n in l:
        if n > max2 and n!=max1:
            max2 = n
    return max2
# print(sec_large((list(map(int,input("Enter a list : ").split())))))


def getSecMax(l):
    if len(l) <=1:
        return None
    lar = l[0]
    slar = None
    for x in l[1:]:
        if x > lar:
            slar = lar 
            lar = x
        elif x!=lar:
            if slar == None or slar<x:
                slar = x
    return slar

print(getSecMax([10,20,30,23,23,11,24]))

