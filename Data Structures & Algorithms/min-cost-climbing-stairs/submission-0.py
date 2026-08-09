class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        for step in range(2, n + 1):
            dp[step] = min(dp[step-1] + cost[step-1],
                            dp[step-2] + cost[step-2])
        return dp[n] #end of steps cost?
