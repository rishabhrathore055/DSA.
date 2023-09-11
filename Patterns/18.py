"""
        A
      A B C        
    A B C D C      
  A B C D E D C    
A B C D E F E D C 
"""
n = int(input("Enter the number : "))
for i in range(n):
    for j in range(0,n-i-1):
        print(" ",end=" ")
    ch = 65
    breakpoint = (2*i+1)/2
    for j in range(0,2*i+1):    
        print(chr(ch),end=" ")
        if(j<=breakpoint) : ch+=1
        else : ch -=1
    for j in range(0,n-i-1):
        print(" ",end=" ")
    print(" ")