class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def dfs(i, curr):
            #if we have target, append subset
            if sum(curr) == target:
                res.append(curr[:])
                return
            #skip out of bounds
            if i >= len(candidates) or sum(curr) > target:
                return

            curr.append(candidates[i]) #add on candidate
            dfs(i + 1, curr) #advance i
            curr.pop() #pop off candidate
            #skip duplicates
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            #try advance with non duplicate
            dfs(i + 1, curr)
            
        dfs(0,[])
        return res