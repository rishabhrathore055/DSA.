 #naive
def maxSum(nums,k):
    n = len(nums)
    maxsum = -1
    for i in range(n):
        sum = 0
        for j in range(k):
            sum += nums[j]
        maxsum = max(maxsum,sum)
    return maxsum
print(maxSum([1,5,4,2,9,9,9],3))