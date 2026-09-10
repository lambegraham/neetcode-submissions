class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        subset = []
        res = []

        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())

            
            for num in nums:
                if num not in subset:
                    subset.append(num)
                    dfs()
                    subset.pop()
        dfs()
        return res
            
