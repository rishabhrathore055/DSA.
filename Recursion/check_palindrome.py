def check_palindrome(st,s,e):
    if s == e:
        return True
    if(st[s]!=st[e]):
        return False
    if (s<e +1):
        return check_palindrome(st,s+1,e-1)
    return True

def check_palin(i,s):
    if i >= len(s)//2:
        return True
    if(s[i]!=s[len(s)-i-1]):
        return False
    return check_palin(i+1,s)
print(check_palin(0,"madam",))