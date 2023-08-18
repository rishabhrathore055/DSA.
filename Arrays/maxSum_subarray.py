def maxSum(nums):
    res = nums[0]
    for i in range(len(nums)):
        curr = 0
        for j in range(i,len(nums)):
            curr = curr + nums[j]
            res = max(res,curr)
    return res
print(maxSum([2,3,-8,7,-1,2,3]))
        