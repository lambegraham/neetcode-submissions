class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def dfs(i, curr):

            if sum(curr) == target:
                res.append(curr.copy())
                return #exit

            if sum(curr) > target or i >= len(candidates):
                return #exit

            
            curr.append(candidates[i]) #choose
            dfs(i+1, curr)
            curr.pop()
            #skip branch, no duplicates allowed so need to make sure not same num
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr)

        dfs(0,[])
        return res
