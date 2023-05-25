# https://practice.geeksforgeeks.org/problems/armstrong-numbers2727/1

class Solution:
    def armstrongNumber (ob, n):
        temp = n
        Sum = 0
        while n > 0:
            last  = n % 10
            Sum = Sum + pow(last,3)
            n//=10
        return "Yes" if Sum == temp else "No"
    

s = Solution()
print(s.armstrongNumber(371))

