def f(n):
    if n == 0:
        return
    else:
        f(n-1)
        print(n)
        f(n-1)
        print(n)
(f(3))