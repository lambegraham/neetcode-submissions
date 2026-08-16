class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        openCount = 0
        closeCount = 0
        res = []
        subset = []

        def bt(oC, cC):
            if(oC == n and cC == n):
                res.append("".join(subset))
                return

            if oC < n:
                subset.append("(")
                bt(oC + 1, cC)
                subset.pop()

            if cC < oC:
                subset.append(")")
                bt(oC, cC + 1)
                subset.pop()
        bt(0,0)
        return res