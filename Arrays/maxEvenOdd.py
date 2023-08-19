def maxLengthEvenOdd(nums):
        res = 1
        curr = 1
        for i in range(len(nums)):
            if ((nums[i]%2==0 and nums[i-1]%2!=0) or (nums[i]%2!=0 and nums[i-1]%2==0)):
                curr+=1
                res = max(res,curr)
            else:
                curr = 1
        if(res == 1):
            return 0
        return res
print(maxLengthEvenOdd([10,12,14,7,8]))