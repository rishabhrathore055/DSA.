"""
A
A B
A B C
A B C D
A B C D E
"""
n = int(input("Enter the value of n : "))
num = 65
for i in range(n+1):
    for j in range(i):
        print(chr(num+j),end=" ")
    print()
