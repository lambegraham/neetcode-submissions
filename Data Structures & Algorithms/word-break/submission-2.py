class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set(wordDict)
        memo = {}
        def dfs(i):

            if i in memo:
                return memo[i]
                
            if i == len(s):
                return True # consumed the entire string successfully
            
            for j in range(i, len(s)):
                 # check whether s[i:j+1] is a valid word
                if s[i : j + 1] in wordSet:
                    # continue from the character after this matched word
                    if dfs(j + 1):
                        memo[i] = True
                        return memo[i]
            memo[i] = False
            return memo[i]
        return dfs(0)