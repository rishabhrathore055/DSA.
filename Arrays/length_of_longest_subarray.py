def longestSubarry( nums):
    res = 0
    count = 0
    for n in nums:
        if n>=0:
            count+=1
        else:
            count = 0
        res = max(count,res)
    return count

def longestSubarry( nums):
    res = 0
    count = 0
    for n in nums:
        if n<0:
            count = 0
        else:
            count+=1
        res = max(count,res)
    return res
    
    
print(longestSubarry([1,-2,3,2,12,-1,2]))