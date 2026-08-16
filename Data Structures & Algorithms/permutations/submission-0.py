class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        sub = []
        res = []

        def dfs():
            if len(sub) == len(nums):
                res.append(sub[:])
                return

            for num in nums:
                if num in sub:
                    continue
                sub.append(num)
                dfs()
                sub.pop()
        dfs()
        return res