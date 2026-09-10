class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]

            cache[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return cache[i]
            #i + 1 = skip current house
            #nums[i] + 1+2 = rob current house, skip next
        return dfs(0)