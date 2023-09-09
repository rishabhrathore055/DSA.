"""

"""
n = int(input("Enter the value of n : "))
space = 2 *(n - 1)
for i in range(1,n+1):
    # numbers
    for j in range(1,i+1):
        print(j,end="")

    # space
    for j in range(space):
        print(end=" ")

    # numbers
    for j in range(i,0,-1):
        print(j,end="")
    print()
    space-=2
