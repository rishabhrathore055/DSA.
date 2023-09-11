def rev_an_arr(nums,start,end):
    if (start>=end):
        return
    nums[start],nums[end] = nums[end], nums[start]
    rev_an_arr(nums,start+1,end-1)

nums = [1, 2, 3, 4, 5, 6]
rev_an_arr(nums, 0, 5)
print("Reversed list is")
print(nums) 
  