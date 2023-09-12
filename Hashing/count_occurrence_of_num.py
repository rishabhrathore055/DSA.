# Q1 - Write a program to count the number of times each word occurs in an array
def countOccurrences(nums):
    hmap = {}
    for e in nums:
        if e in hmap:
            hmap[e] += 1
        else:
            hmap[e] = 1
    for k,v in hmap.items():
        print(k,v)
countOccurrences([1,1,2,3,2,3,1,4,4,5,6,5])
