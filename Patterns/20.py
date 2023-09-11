"""
* * * * * * * *
* * *     * * *
* *         * *
*             *
*             *
* *         * *
* * *     * * *
* * * * * * * *

"""
n = int(input("Enter the number : "))
space = 0
for i in range(n):
    # stars
    for j in range(1,n-i):
        print("*",end = " ")
    # spaces
    for j in range(0,space):
        print(" ",end = " ")
    # stars
    for j in range(1,n-i):
        print("*",end = " ")
    space+=2
    print()
space = n*2-2
for i in range(n):
    # stars
    for j in range(i):
        print("*",end = " ")
    # spaces
    for j in range(0,space):
        print(" ",end = " ")
    # stars
    for j in range(i):
        print("*",end = " ")
    space-=2
    print()