nums = [1,2,3,4,5,6]
print("Array before rotated")
for i in range(len(nums)):
    print(nums[i],end=" ")
print("\r")

k = int(input("Enter the times have to rotated the array: "))
def rotate(nums, k):

    n = len(nums)
    k = k % n
    nums[:] = nums[n-k:] + nums[:n-k]
    return nums

print(rotate(nums, k))