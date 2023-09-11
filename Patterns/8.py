# https://practice.geeksforgeeks.org/problems/triangle-pattern-1661493231/1
"""
* * * * * * * * * * *
  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *
"""
n = int(input("Enter the number : "))
for i in range(0,n):
    for j in range(0,i):
        print(" ",end=" ")
    for j in range(0,(2*n-(2*i+1))):
        print("*",end=" ")
    for j in range(0,i):
        print(" ",end=" ")
    print(" ")