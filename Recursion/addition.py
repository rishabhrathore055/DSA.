def addition(x,y):
    if y == 0:
        return x
    return addition(x,y-1)+1
print(addition(10,20))