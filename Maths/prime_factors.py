def isNum(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5,int(n**0.5)+1,6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

def primeFactors(n):
    if n == 1:
        return 1
    if isNum(n):
        return n
    res = 1
    for i in range(2,n+1):
        if isNum(i):
            count = 0
            while n % i == 0:
                count += 1
                n //= i
                print(i)
            res *= (i**count)
    return res
print(primeFactors(12))