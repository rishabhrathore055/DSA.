"""
        A
      B B B
    C C C C C
  D D D D D D D    
E E E E E E E E E
"""
n = int(input("Enter the number : "))
num = 65
for i in range(n):
    for j in range(0,n-i-1):
        print(" ",end=" ")
    for j in range(0,2*i+1):
        print(chr(num),end=" ")
    for j in range(0,n-i-1):
        print(" ",end=" ")
    print(" ")
    num+=1