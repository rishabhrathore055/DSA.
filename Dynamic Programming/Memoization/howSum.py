"""
Writea program that takes in a targetSum and an array of numbers as arguments.
The function should return an array containing  any combination of elements that add up to exactly the target sum 
if there is no combination that adds upto the targetSum, then return null.
numbers from array.

if there are multiple combinations possible, you may return any single one.
"""

# Without memo
def howSum(targetSum,nums):
    ans = []
    if (targetSum == 0): return []
    if (targetSum <0): return None
    for num in nums:
        remainder = targetSum - num
        remainderRemain =howSum(remainder,nums)
        if remainderRemain is not None:
            return remainderRemain + [num]
    return None
print(howSum(7,[2,3]))
# print(howSum(300,[2,3,5,6]))
