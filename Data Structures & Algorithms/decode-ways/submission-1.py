class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def dfs(i):

            if i in cache:
                return cache[i]

            if i == len(s):
                return 1

            if s[i] == '0':
                return 0

            res = dfs(i+1)

            if i < len(s) - 1 and 10 <= int(s[i:i+2]) <= 26:
                res += dfs(i+2)
            
            cache[i] = res
            return cache[i]
        return dfs(0)