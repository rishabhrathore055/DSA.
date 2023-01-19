def binary_search(arr,first,last,target):
    if last >= first:
        mid = first + (last - first) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr,first,mid-1,target)
        else:
            return binary_search(arr,mid+1,last,target)
    else:
        return -1

arr = [1,2,3,4,5,6,7,8,9,10]
target = 5
result = binary_search(arr,0,len(arr)-1,target)
print(result)
    
