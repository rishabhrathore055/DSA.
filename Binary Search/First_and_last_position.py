def searchRange(nums, target):
    start,end = 0, len(nums)-1
    first, last = -1,-1
    res = []
    while start<=end:
        mid = start + (end-start)//2
        if target == nums[mid]:
            first = mid
            end = mid-1
        elif target> nums[mid]:
            start = mid+1
        else:
            end =  mid-1
    end = len(nums) -1
    while start<=end:
        mid = start + (end-start)//2
        if target == nums[mid]:
            last = mid
            start = mid +1
        elif target> nums[mid]:
            start = mid+1
        else:
            end =  mid-1
    res.append(first)
    res.append(last)
    return res
print(searchRange([5,7,7,8,8,10],8))