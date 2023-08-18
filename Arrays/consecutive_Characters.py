def maxPower(s: str) -> int:
    count = 0
    maxCount = 0
    previous = None
    for c in s:
        if c == previous:
            count+=1
        else:
            previous = c
            count = 1
        maxCount = max(count,maxCount)
    return maxCount

print(maxPower("Leetcode"))
