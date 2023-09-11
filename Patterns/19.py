"""
E
E D
E D C
E D C B
E D C B A
"""
n = int(input("Enter the number : "))
num = 65 
for i in range(0,n):
    for j in range(i+1): 
        print(chr(num+n-j-1),end =" ")
    print()