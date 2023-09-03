# https://leetcode.com/problems/is-subsequence/

# itrative solutions
def isSubsequence(s1,s2):
    n = len(s1)
    m = len(s2)
    i,j = 0 , 0

    while i!=n and j!=m:
        if (s1[i] == s2[j]):
            j+=1
        i+=1
    return j == m
print(isSubsequence("ABCD","AD"))


# recursion solution
def isSubsequenceRec(s,t,n,m):
    if m == 0 :return True
    if n == 0 :return False
    if (s[n-1]==t[m-1]):
        return isSubsequenceRec(s,t,n-1,m-1)
    else:
        return isSubsequenceRec(s,t,n-1,m)

print(isSubsequenceRec("ABCD","AD",4,2))