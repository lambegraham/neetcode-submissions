class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        sub = []
        res = []

        def dfs():
            #base case?
            if len(sub) == len(nums):
                res.append(sub.copy()) #deep copy

            for num in nums:
                if num not in sub:
                    sub.append(num)
                    dfs()
                    sub.pop()
                    
        dfs()
        return res