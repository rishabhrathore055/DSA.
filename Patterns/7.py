# https://practice.geeksforgeeks.org/problems/triangle-pattern-1661492263/1
"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
n = int(input("Enter the number : "))
for i in range(n):
    for j in range(0,n-i-1):
        print(" ",end=" ")
    for j in range(0,2*i+1):
        print("*",end=" ")
    for j in range(0,n-i-1):
        print(" ",end=" ")
    print()