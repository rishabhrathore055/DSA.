# https://practice.geeksforgeeks.org/problems/square-pattern/1
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
n = int(input("Enter the number : "))
for i in range(n):
    for j in range(n):
        print("*",end =" ")
    print()
