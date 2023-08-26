def prefixsum(nums):
    n = len(nums)
    prefixsum = [n]
    prefixsum[0] = nums[0]
    for i in range(1,n):
        prefixsum.append(prefixsum[i-1] + nums[i])
    return prefixsum
print(prefixsum([2,8,3,9,6,5,4]))