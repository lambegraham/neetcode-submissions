class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        sub = []
        nums.sort()

        def dfs(i, curr):

            if i == len(nums) and curr not in res:
                res.append((curr.copy()))
                return

            
            if i >= len(nums):
                return
            
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()
            dfs(i+1, curr)
        
        dfs(0, [])
        return res