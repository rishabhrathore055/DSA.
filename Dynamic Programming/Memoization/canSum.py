"""
Writea program that takes in a targetSum and an array of numbers as arguments.
The function should return a boolean indicating whether or not it is possiable to generatr the targetSum using
numbers from array.
"""
# Without memo
# def canSum(targetSum,nums):
#     if (targetSum == 0): return True
#     if (targetSum <0): return False
#     for num in nums:
#         remainder = targetSum - num
#         if (canSum(remainder,nums) == True): return True
#     return False

# print(canSum(7,[2,3]))
# print(canSum(300,[2,3,5,6]))



def canSum(targetSum,nums,memo = {}):
    if (targetSum in memo): return  memo[targetSum]
    if (targetSum == 0): return True
    if (targetSum <0): return False
    for num in nums:
        remainder = targetSum - num
        if (canSum(remainder,nums,memo) == True): return True
        memo[targetSum] = True
    memo[targetSum] = False
    return False

print(canSum(11,[1,2,5]))
# print(canSum(8,[2,3,5]))
# print(canSum(300,[7,14]))
