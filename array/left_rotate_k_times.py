# Method one
def leftRotate(l,d):
    for i in range(0,d):
        l.append(l.pop(0))
    return l   
print(leftRotate([1,2,3,4,5],2))