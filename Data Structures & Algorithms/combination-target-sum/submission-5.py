class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr): #i = index, curr = current values in []
            #RES

            if sum(curr) == target:
                res.append(curr.copy()) #append a list of chars to res
                return

            #OOB
            if i >= len(nums) or sum(curr) > target:
                return

            #Backtracking
            curr.append(nums[i]) #make the choice
            dfs(i, curr) #run DFS on choice
            curr.pop() #undo choice
            dfs(i + 1, curr) #run DFS again

        dfs(0, [])
        return res