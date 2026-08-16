class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr):

            if sum(curr) == target:
                res.append(curr[:])
                return

            if i >= len(nums) or sum(curr) > target:
                return
            
            curr.append(nums[i])
            dfs(i, curr)
            curr.pop()
            dfs(i + 1, curr)
        dfs(0,[])
        return res