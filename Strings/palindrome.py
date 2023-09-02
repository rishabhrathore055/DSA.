def palindrome():
    s = input("Enter the strings : ")
    if len(s) == 0: return s
    l,r = 0,len(s)-1
    
    while(r>l):
        if s[l] != s[l]:
            return False
        l+=1
        r-=1
    return True
print(palindrome())