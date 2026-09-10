class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i] #cache
            if i == n:
                return 1 #valid
            if i > n:
                return 0 #invalid
            
            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]
        return dfs(0)