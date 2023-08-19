def maxSum(nums): # naive
    res = nums[0]
    for i in range(len(nums)):
        curr = 0
        for j in range(i,len(nums)):
            curr = curr + nums[j]
            res = max(res,curr)
    return res

def maxsum(nums): # efficient
    maxEnding = nums[0]
    res = nums[0]
    for i in range(len(nums)):
        maxEnding = max(maxEnding + nums[i],nums[i])
        res = max(res,maxEnding)
    return res
print(maxSum([5,4,-1,7,8]))
print(maxsum([-2,1,-3,4,-1,2,1,-5,4]))
        