# naive
# https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1
def maximizeSum(nums, k):
        max_sum = max(nums)
        n = len(nums)
        for i in range((n-k)+1):
            sum = 0
            for j in range(i,i+k):
                sum+=nums[j]
            max_sum = max(sum,max_sum)
        return max_sum


# optimize
def MaxiSum(nums, k):
    n = len(nums)
    i = 0 
    j = 0
    Sum = 0
    maxSum = min(nums)
    while j < n:
        Sum = Sum + nums[j]
        if(j-i+1==k):
            maxSum = max(Sum,maxSum)
            Sum = Sum - nums[i]
            i+=1
        j+=1
    return maxSum
print(MaxiSum([1,8,30,-5,20],3))