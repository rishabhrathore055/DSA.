# naive solutions # TP O(nlogn)
def anagram(s1,s2):
 if len(s1)!=len(s2): return False
 s1 = sorted(s1)
 s2 = sorted(s2)
 return s1 == s2
print(anagram("abbc","acbb"))

def areAnagram(s1,s2):
    if len(s1) != len(s2): return False
    count = [0]*256
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1

    for x in count:
        if x!=0:
            return False
    return True
print(areAnagram("abbc","acbb"))

# Using hashmap 
def isAnagram(s,t) -> bool:
        if(len(s)!=len(t)):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        for c in countS:
            if (countS[c]!= countT.get(c,0)):
                return False
        return True 
print(isAnagram("abbc","acbb"))
