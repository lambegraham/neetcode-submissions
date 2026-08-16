class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
        nums.sort()

        def dfs(i):
            if i == len(nums):
                if subset in res:
                    return
                res.append(subset[:])
                return 

            # while nums[i] in subset:
            #     i += 1
            
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res
            