class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        dp = {} #(i, total) = 
        
        def dfs(i, sum):
            if i == len(nums):
                if sum == target:
                    return 1
                else:
                    return 0
            
            if(i, sum) in dp:
                return dp[(i, sum)]
            
            num = nums[i]
            dp[(i,sum)] = (dfs(i + 1, sum + num) + dfs(i + 1, sum - num))
            return dp[(i, sum)]
        return  dfs(0,0)