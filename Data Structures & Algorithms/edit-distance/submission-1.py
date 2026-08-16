class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        w1, w2 = len(word1), len(word2)
        dp = {}
        
        def dfs(i, j):
            if i == w1:
                return w2 - j
            if j == w2:
                return w1 - i
            if (i, j) in dp:
                return dp[(i, j)]

            if word1[i] == word2[j]: #word is same so far, continue
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                #delete from w1, add to w1
                res = min(dfs(i + 1, j), dfs(i, j + 1))
                #or replace in w1
                res = min(res, dfs(i + 1, j + 1))
                dp[(i, j)] = res + 1

            return dp[(i,j)]
        return dfs(0,0)

