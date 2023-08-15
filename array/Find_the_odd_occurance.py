def findOdd(l1):
    count ={}
    for n in l1:
        if n in count:
            count[n] +=1
        else:
            count[n] = 1
    for k,v in count.items():
        if v%2!=0:
            return k
def find_odd(l):
    res = 0
    for x in l:
        res ^= x
    return res
print(find_odd([10,10,10,20,20,30,30]))