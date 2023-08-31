# Without the memoization
# def fib(n):
#     if (n<=2):
#         return 1
#     return fib(n-1) + fib(n-2)


# Memoization - Reminder for myself
# bottom up approach
# def Fibo(n):
#     fibTable = [0,1]
#     for i in range(2,n+1):
#         fibTable.append(fibTable[i-1]+fibTable[i-2])
#     return fibTable[n]
# print(Fibo(160))


# with space complexity O(1)
def Fibo(n):
    a,b = 1,0
    for i in range(n):
        a,b = b,a+b
    return a
print(Fibo(10))



# Top Down approach
def fib(n,memo = {}):
    if (n in memo) :return memo[n]
    if (n<=2):
        return 1
    memo[n] = fib(n-1,memo) + fib(n-2,memo)
    return memo[n]

print(fib(1))
print(fib(7))
print(fib(58))
print(fib(160))
