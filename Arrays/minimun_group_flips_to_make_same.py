def PrintGrupo(nums):
    n = len(nums)
    for i in range(n):
        if(nums[i]!=nums[i-1]):
            if(nums[i]!=nums[0]):
                print("From %s to"%i)
            else:
                print(i-1)
    if(nums[n-1]!=nums[0]):
        print(n-1)

print(PrintGrupo([1,1,0,0,0,1]))