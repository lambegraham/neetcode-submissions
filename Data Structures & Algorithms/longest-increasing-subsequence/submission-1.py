class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i, j): #i = current index deciding on, j = index of last number chosen
            if (i, j) in cache:
                return cache[(i,j)]

            if i == len(nums):
                return 0

            LIS = dfs(i + 1, j)  #do not incl
            
            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i)) #choose i as last index
            cache[(i,j)] = LIS
            return LIS
        
        return dfs(0, -1)