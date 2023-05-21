def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n

n = int(input("ENTER A NUMBER: "))
print(factorial(n))

