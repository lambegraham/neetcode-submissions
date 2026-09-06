class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        #[2,3,4]
        #[0,0,0] [2,2,2] 2, [2,3,3] 3, [2,3,4] 4
        res = 0

        def dfs(l,r,height):
            nonlocal res

            if l > r:
                return 

            minVal = min(target[l:r + 1])
            res += minVal-height

            start = l

            for i in range(l, r + 1):
                if target[i] == minVal:
                    dfs(start, i - 1, minVal)
                    start = i + 1
            dfs(start, r, minVal)

        dfs(0, len(target)-1, 0)
        return res