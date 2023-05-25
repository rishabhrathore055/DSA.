import math
class Solution:
    def sumOfDivisors(self, N):
        ls = []
        for i in range(1,round(math.sqrt(N))):
            if N % i == 0:
                ls.append(i)
                if (N//i) != i:
                    ls.append(N//i)
        return sorted(ls)
    
s = Solution()
print(s.sumOfDivisors(36))