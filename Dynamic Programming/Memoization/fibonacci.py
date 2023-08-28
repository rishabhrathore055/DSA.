# Without the memoization
# def fib(n):
#     if (n<=2):
#         return 1
#     return fib(n-1) + fib(n-2)


# Memoization - Reminder for myself
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
