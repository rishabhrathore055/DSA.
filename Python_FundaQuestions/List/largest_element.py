def largest(l):
    max = 0
    for n in l:
        if n > max: max = n
    return max

print(largest((list(map(int,input("Enter a list : ").split())))))