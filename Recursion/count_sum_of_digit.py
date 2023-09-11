def sum_of_d(n):
    if n<=9:
        return n
    else:
        return n%10 + sum_of_d(n//10)
print(sum_of_d(111))