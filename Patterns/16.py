"""
A
B B
C C C
D D D D
E E E E E

"""
n = int(input("Enter the value of n : "))
num = 65
for i in range(1,n+1):
    for j in range(i):
        print(chr(num),end=" ")
    print()
    num+=1
