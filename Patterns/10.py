"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
n = int(input("Enter the value of n : "))

for i in range(1,2*n-1):
    stars = i
    if(stars > n):
        stars = 2*n-i
    for j in range(1,stars):
        print("*",end=' ')
    print()