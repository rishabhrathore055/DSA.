# naive solutions
def remove_duplicate(nums,n):
    res = 0
    for i in range(1,n):
        if nums[res]!=nums[i]:
            res+=1
            nums[res]= nums[i]
    return res+1

print(remove_duplicate([10,20,30,30,30],5))
