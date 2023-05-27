class Solution:
    def checkPrime(self,n):
        if n == 1:
            return 0
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    def minJumps(self, arr, n):
        res = 0
        for n in arr:
            res+=self.checkPrime(n)
        return res
    
s = Solution()
print(s.minJumps([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],25))              