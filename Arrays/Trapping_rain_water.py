from typing import List
def trap(nums: List[int]) -> int:
    left = 0
    right = len(nums)-1
    res = 0
    maxleft = 0
    maxright = 0
    while left <= right:
        if(nums[left]<=nums[right]):
            if(nums[left]>= maxleft) : maxleft = nums[left]
            else : res+= maxleft - nums[left]
            left+=1
        else:
            if(nums[right]>= maxright) : maxright = nums[right]
            else : res+= maxright - nums[right]
            right-=1
    return res

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))