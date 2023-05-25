# https://practice.geeksforgeeks.org/problems/count-digits5716/1

class Solution:
    def evenlyDivides (self, N):
        temp = N
        count = 0
        while N > 0:
            digit = N % 10
            N  = N/10
            if digit!=0 and temp%digit == 0:
                count+=1
        return count
s = Solution()
print(s.evenlyDivides(1232))