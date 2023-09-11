def nto1(n):
    if n == 0:
        return
    print(n)
    return nto1(n-1)
print(nto1(5))