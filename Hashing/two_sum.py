
# Q4 - Write a program to check if arr[i] + arr[j] = k and i != j

def twoSum(arr,k): ## tc = O(n^2)
    for i in range(len(arr)): 
        for j in range(i,len(arr)):
            if arr[i] + arr[j] == k and i != j:
                return (arr[i],arr[j])
print(twoSum([1,3,2,3,8,9],4))

def Twosum(nums,target):
    hset = set() ## tc = O(n) using hashset
    for i in range (len(nums)):
        r = target - nums[i]
        if r in hset:
            return [nums.index(r),i]
        else:
            hset.add(nums[i])

print(Twosum([1,2,4,5,6],9))

def TwoSum(arr,k):
    hmap = {} ## tc = O(n) using hashmap
    for i in arr:
        print(i)
        r = k - i
        if r in hmap:
            print(i,r)
            break
        else:
            hmap[i] = 1