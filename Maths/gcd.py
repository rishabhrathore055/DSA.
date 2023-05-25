https://practice.geeksforgeeks.org/problems/lcm-and-gcd4516/1
def gcd(a,b):
    while a>0 and b>0:
        if a>b:
            a = a%b
        else:
            b = b % a
    if a == 0:
        return b
    else:
        return a

print(gcd(52,10))