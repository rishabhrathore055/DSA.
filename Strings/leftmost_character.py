# https://leetcode.com/problems/first-unique-character-in-a-string

#naive solution O(n^2)
def leftmostchar(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]: return i
    return -1
print(leftmostchar("ABCDAC"))


# Better approach
def leftmostChar(s):
    count = {}
    for char in s:
        if char in count:
            count[char]+=1
        else:
            count[char] =1
    for i in range(len(count)):
        if count[s[i]] > 1:
            return i
    return -1
print(leftmostChar("AKABJAOUDESABCDA"))
