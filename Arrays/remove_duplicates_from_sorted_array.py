# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for i in range(1,len(nums)):
            if nums[i]!=nums[index]:
                index+=1
                nums[index] = nums[i]
        return index+1
s = Solution()
        
print(s.removeDuplicates([1,2,3,2,23,23]))
