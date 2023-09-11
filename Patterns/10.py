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

for i in range(2*n):
    stars = i
    if(stars > n):
        stars = 2*n-i
    for j in range(1,stars+1):
        print("*",end=' ')
    print()