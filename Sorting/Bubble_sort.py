# push the max to the end by adjacent swaps
def bubble_Sort(nums,n): # O(n^2)
    def Swap(nums,a,b):
        nums[a],nums[b] = nums[b],nums[a]
        return nums
    for i in range(n,0,-1):
        for j in range(0,i-1):
            if nums[j] > nums[j+1]:
                Swap(nums,j,j+1)
    return nums
print(bubble_Sort([23,1,22,12,2,24],6))


    