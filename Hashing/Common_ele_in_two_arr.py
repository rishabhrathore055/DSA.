
# Q3 - Write a program to  find the common elements between two arrays
def common_elements(nums1, nums2):
    hmap = {}
    res = []
    for i in nums1:
        if i in hmap:
            hmap[i]+=1
        else:
            hmap[i] = 1
    for j in nums2:
        if j in hmap:
            res.append(j)
            del hmap[j]
    return res
print(common_elements([1,1,2,3,4,3],[1,3,4]))


# nums1 = set(nums1) # Use set to remove duplicates
# ans = []
# for num in nums2:
#     if num in nums1:
#         ans.append(num)
#         nums1.remove(num)
# return res

