# Method first with O(n) time complexity
arr = [2,3,5,6,8,7]
arr2 = []
j = 0
for i in range(len(arr)-1,-1,-1):
    arr2.append(arr[i])
    j = j+1
for i in range(0,len(arr)):
    arr[i] = arr2[i]
# print(arr)

# Method 2 with O(n/2) time complexity
arr1 = [2,8,24,12,6,3,10]
j = len(arr1)-1
i = 0
print(arr1)
while(i<=j):
    temp = arr1[i]
    arr1[i] = arr1[j]
    arr1[j] = temp
    i+=1
    j-=1
print(arr1)
