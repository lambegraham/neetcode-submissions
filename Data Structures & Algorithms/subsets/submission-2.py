class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []
        res = []
        def dfs(i):
            if len(nums) == i:
                res.append(subsets.copy())
                return 

            subsets.append(nums[i])
            dfs(i + 1)
            subsets.pop()
            dfs(i + 1)

        dfs(0)
        return res