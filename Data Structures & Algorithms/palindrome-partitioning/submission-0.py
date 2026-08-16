class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []

        def dfs(i):
            if i == len(s):
                res.append(sub[:])

            for end in range(i, len(s)):
                part = s[i : end + 1]
            
                if part == part[::-1]:
                    sub.append(part)
                    dfs(end + 1)
                    sub.pop()
        dfs(0)
        return res