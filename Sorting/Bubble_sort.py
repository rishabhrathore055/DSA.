# push the max to the end by adjacent swaps
def bubble_Sort(nums,n): # O(n^2) Worst and best Time complexity is O(n)
    def Swap(nums,a,b):
        nums[a],nums[b] = nums[b],nums[a]
        return nums
    didSwap = 0
    for i in range(n,0,-1):
        for j in range(0,i-1):
            if nums[j] > nums[j+1]:
                Swap(nums,j,j+1)
                didSwap = 1
        print(didSwap)
        if didSwap == 0:
            break
    return nums
print(bubble_Sort([1,2,3,4],4))


    