#naive solutions
def feqencies_of_ele(nums):
    n = len(nums)
    freq = i = 1
    while (i<n):
        while(i < n and nums[i]==nums[i-1]):
            freq+=1
            i+=1
        print(nums[i-1],freq)
        i+=1
        freq=1
    if n==1 or nums[n-1] != nums[n-2]:
        print(nums[n-1],1)

print(feqencies_of_ele([40,50,50,50,60]))
