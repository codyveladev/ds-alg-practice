#O(nlogn) solution 
class Solution1:
    def countBits(self, n: int):
        ans = []
        #O(n)
        for i in range(n + 1): 
            ans.append(self.convertToNumOfOnes(i))
        return ans 
    #O(logn)
    def convertToNumOfOnes(self, n): 
        count = 0
        while n != 0: 
            if n % 2 == 1: 
                count += 1 
            n //= 2
        return count        

#O(n) solution 
class Solution2:
    def countBits(self, n: int):
        dp = [0] * (n + 1)
        offset = 1 
        for i in range(1, n + 1): 
            if offset * 2 == i: 
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp    