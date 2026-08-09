class Solution:
    def climbStairs(self, n: int) -> int:
        #start at 0, call climbStairs with either n or n+1. return 1 each way
        cache = [-1] * n 

        def climb(i):
            if i == n:
                return 1 #valid path
            if i > n:
                return 0 #invalid path
            if cache[i] != -1:
                return cache[i]
            cache[i] = climb(i + 1) + climb(i + 2)
            return cache[i]
        return climb(0)