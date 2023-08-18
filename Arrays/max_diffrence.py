#Naive
def maximumDifference(nums):
        res = (nums[1]-nums[0])
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                res = max(res,(nums[j]-nums[i]))
        return res

print(maximumDifference([2,3,10,6,3,8,1]))


# efficient 
def maxDiff(nums):
    res = (nums[1]-nums[0])
    minval = nums[0]
    for i in range(len(nums)):
        res = max(res,(nums[i]-minval))
        minval = min(minval,nums[i])
    return res
print(maxDiff([2,3,10,6,3,8,1]))