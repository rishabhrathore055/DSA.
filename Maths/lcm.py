# naive approach
def lcm(a,b):
    res = max(a,b)
    while True:
        if res % a == 0 and res % b == 0:
            return res
        res += 1
    return res
print(lcm(12,16))

# efficient approach
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
def lcm(a,b):
    return (a*b)//gcd(a,b)
print(lcm(12,16))