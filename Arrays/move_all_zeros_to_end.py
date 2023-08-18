# Naive solutions // n^2
def move_zero(nums):
    for i in range(len(nums)):
        if(nums[i]==0):
            for j in range(i+1,len(nums)):
                if nums[j]!=0:
                    nums[i],nums[j] = nums[j],nums[i]
    return nums


# optimal solutions
def moveZero(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[i],nums[count] = nums[count],nums[i]
            count += 1
    return nums
print(moveZero([10,5,0,0,8,0,9,0]))
