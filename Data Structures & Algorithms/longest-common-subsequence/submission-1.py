class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def dfs(i, j): #return longest common subsequence [INT]

            if (i, j) in cache:
                return cache[(i,j)]

            if i == len(text1) or j == len(text2):
                return 0
            
            if text1[i] == text2[j]: #if the char is the same
                return 1 + dfs(i+1, j+1) #recurse and add 1 to result
            cache[(i,j)] = max(dfs(i+1, j), dfs(i, j+1))
            return cache[(i,j)]
        return dfs(0,0)