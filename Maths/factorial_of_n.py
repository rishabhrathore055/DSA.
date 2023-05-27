# itrative method

def factorial(n):
    res = 1
    for i in range(1,n+1):
        res = res * i
    return res

print(factorial(5))

# recursive method
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# print(factorial(5))