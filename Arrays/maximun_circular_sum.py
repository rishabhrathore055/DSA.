# Naive solution with O(n^2)
def maximumCircularSum(nums):
    n = len(nums)
    res = nums[0]
    for i in range(n):
        curr_sum = nums[i]
        curr_max = nums[i]
        for j in range(1,n):
            index = (i + j) %n
            curr_sum += nums[index]
            curr_max =  max(curr_max, curr_sum)
        res = max(res, curr_max)
    return res



def maxiCircularSum(nums):
    curMax,curMin = 0,0
    globalmax,globalmin = nums[0],nums[0]
    total = 0 
    for n in nums:
        curMax = max(curMax+n,n)
        curMin = min(curMin+n,n)
        total+=n
        globalmax = max(globalmax,curMax)
        globalmin = min(globalmin,curMin)
    return max(globalmax,total-globalmin) if globalmax > 0 else globalmax

print(maxiCircularSum([10,-5,5]))