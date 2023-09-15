# get the minimum and sort it
def selection_sort(nums,n): # O(n^2)
    def Swap(nums,a,b):
        nums[a],nums[b] = nums[b],nums[a]
        return nums
    for i in range(n-1):
        mini = i
        for j in range(i,n):
            if nums[j]  < nums[mini]:
                mini = j
        Swap(nums,mini,i)
    return nums
print(selection_sort([113,13,12,32,13,25],6))



     