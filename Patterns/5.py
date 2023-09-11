# https://practice.geeksforgeeks.org/problems/triangle-pattern/1?
"""
* * * * *
* * * *
* * *
* *
*
"""
n = int(input("Enter the number : "))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end =" ")
    print()