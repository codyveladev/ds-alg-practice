class Solution:
    def fib(self, n: int) -> int:
        #Bottom up approach
        dp = [0] * (n + 1)
        dp[0] = 0 
        for i in range(1, n+1): 
            if i <= 2: 
                dp[i] = 1
            else: 
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]