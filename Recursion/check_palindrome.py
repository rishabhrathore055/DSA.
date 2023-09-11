def check_palindrome(st,s,e):
    if s == e:
        return True
    if(st[s]!=st[e]):
        return False
    if (s<e +1):
        return check_palindrome(st,s+1,e-1)
    return True

print(check_palindrome("madam",0,4))