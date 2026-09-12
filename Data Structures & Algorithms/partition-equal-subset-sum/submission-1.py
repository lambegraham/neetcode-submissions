class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = {}
        totalSum = sum(nums)
        if totalSum % 2 != 0: return False #cant split odd sum
        
        def dfs(i, target):
            if (i, target) in cache:
                return cache[(i, target)]
            #target reduced to 0 means we could split evenly
            if target == 0: return True
            #could not split evenly
            if i == len(nums) or target < 0: return False

            cache[(i, target)] = dfs(i + 1, target) or dfs(i + 1, target-nums[i])
            return cache[(i, target)]

        return dfs(0, sum(nums) // 2)