class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, curr: List[int], total: int):
            #base case
            if total == target:
                res.append(curr.copy())
                return
            #out of bounds
            if i >= len(nums) or total > target:
                return
            
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i + 1, curr, total)
        dfs(0, [], 0)
        return res