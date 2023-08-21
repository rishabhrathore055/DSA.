def majorityElement(nums):
        n = len(nums)
        for i in range(n):
            count = 1
            for j in range(i+1,n):
                if (nums[i]==nums[j]):
                    count+=1
            if count>n//2:
                return nums[i]
        return -1

print(majorityElement([1,2,2,3,4,2,3,2,2]))