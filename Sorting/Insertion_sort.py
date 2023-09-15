# Take an element and place it in its current position
def insertion_Sort(nums,n): # O(n^2) Worst and best Time complexity is O(n)
    def Swap(nums,a,b):
        nums[a],nums[b] = nums[b],nums[a]
        return nums
    for i in range(n):
        j = i
        while j>0 and nums[j-1] > nums[j]:
            Swap(nums,j-1,j)
            j-=1
    return nums
print(insertion_Sort([21,2,123,4,5],5))


    