# naive solutions # TP O(nlogn)
def anagram(s1,s2):
 if len(s1)!=len(s2): return False
 s1 = sorted(s1)
 s2 = sorted(s2)
 return s1 == s2
print(anagram("abbc","acbb"))


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
