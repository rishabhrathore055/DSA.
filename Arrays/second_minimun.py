def secondmin(nums):
    min1 = max(nums)
    min2 = max(nums)
    for i in range(0,len(nums)):
        if nums[i] < min1:
            min2 = min1
            min1 = nums[i]
        elif nums[i]!=min1:
            if min2>nums[i]:
                min2 = nums[i]
    return min2
print(secondmin([10,10,20,50,80,20,30,30,40]))