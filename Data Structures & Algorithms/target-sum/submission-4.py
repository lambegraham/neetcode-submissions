class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i, sum):
            if i == len(nums):
                if sum == target:
                    return 1 #True
                else:
                    return 0 #False
            
            if (i, sum) in cache:
                return cache[(i, sum)]
             
            num = nums[i]
            cache[(i, sum)] = (dfs(i + 1, sum + num) + dfs(i + 1, sum - num))
            return cache[(i, sum)]
        return dfs(0,0)