def Fibonachi_num(n):
    if n<=2:
        return n
    return Fibonachi_num(n-1) + Fibonachi_num(n-2)
print(Fibonachi_num(5))