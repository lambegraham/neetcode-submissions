class Solution:
    def climbStairs(self, n: int) -> int:
        #n = number of steps
        #return = unique ways to climb to top 
        #can climb 1 or 2 steps at a time
        #n = 3
        #[0] > [1] > [2] > [3] = 3
        #                > [4] = X
        #          > [3] = 2
        #    > [2] > [3] = 2
        #          > [4] = X
        if n<= 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1 #1 step 1 way
        dp[2] = 2 #2 steps 2 ways..
        if n == 0:
            return dp[0]
        if n == 1:
            return dp[1]

        for s in range(3, n+1):
            dp[s] = dp[s - 1] + dp[s - 2]
        return dp[n]
