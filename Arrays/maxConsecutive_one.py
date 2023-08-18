def maxConsecutive(nums): # 0(n) time and 0(1) space
    res = 0
    count = 0
    for n in nums:
        if n == 0:
            count = 0
        else :
            count +=1
            res = max(count,res)
    return res


def maxConsecutive(nums): # 0(n) time and 0(1) space
    res = 0
    count = 0
    for n in nums:
        if n == 1:
            count +=1
            res = max(count,res)
        else:
            count = 0
    return res

print(maxConsecutive([0,1,1,0,1,1,1]))