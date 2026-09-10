class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robber(arr):
            cache = {}
            
            def dfs(i):
                if i >= len(arr):
                    return 0
                if i in cache:
                    return cache[i]
                
                cache[i] = max(dfs(i + 1), arr[i] + dfs(i+2))
                return cache[i]
            
            return dfs(0)
        return max(robber(nums[1:]), robber(nums[:-1]))

        #the first and last are now adjacent
        #use first version, but check by slicing either 1st or -1st house
        #this works because we check for max of both cases