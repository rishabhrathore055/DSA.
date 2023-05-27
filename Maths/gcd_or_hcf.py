# naive approach
def gcd(a,b):
    res = min(a,b)
    while res > 0:
        if a%res == 0 and b%res == 0:
            break
        res -= 1
    return res


print(gcd(12,16))

# euclid's algorithm (recursive)
def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a%b)
    
# print(hcf(12,16))