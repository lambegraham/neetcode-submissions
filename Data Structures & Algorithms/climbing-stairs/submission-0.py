class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n #valid path
            elif cache[i] != -1:
                return cache[i] #already have this answer (memo)
            #from step i, try taking 1 and 2 steps
            #add valid path counts together
            cache[i] = dfs(i + 1) + dfs(i+ 2)
            #save and return total paths from step i
            return cache[i]
        #begin at step 0 until step n
        return dfs(0)

