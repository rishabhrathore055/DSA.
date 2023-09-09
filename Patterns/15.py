"""
A B C D E F
A B C D E
A B C D
A B C
A B
A

"""
n = int(input("Enter the value of n : "))
num = 65
for i in range(n,0,-1):
    for j in range(i):
        print(chr(num+j),end=" ")
    print()
