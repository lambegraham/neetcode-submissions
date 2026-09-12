class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set(wordDict)
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]
            if i == len(s): #we have made all choices
                return True
            
            for j in range(i, len(s)):
                if s[i : j + 1] in wordSet:
                    if dfs(j + 1): #check from j on
                        cache[i] = True
                        return cache[i]
            cache[i] = False
            return cache[i]
        return dfs(0)