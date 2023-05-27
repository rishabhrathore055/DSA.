class Solution:
    def countDigits(self,n):
        count = 0
        while n>0:
            n//=10
            count+=1
        return count
    
s = Solution()
print(s.countDigits(12342))

# recursive
# def rec(n):
#     if(n==0):
#         return 0
#     return 1 + rec(n//10)
# print(rec(123))