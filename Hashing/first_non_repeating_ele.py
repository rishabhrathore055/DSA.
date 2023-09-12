# Q2 - Write a program to display the first non-repeating character in an array

def nonRepeating(nums):
    hmap = {}
    for i in nums:
        if i in hmap:
            hmap[i]+=1
        else:
            hmap[i]= 1
    for k,v in hmap.items():
        if v == 1:
            return k
print(nonRepeating([20,1,7,6,1,20,3,8,20,3,8,7]))