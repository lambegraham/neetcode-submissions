class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #PAIRS: (i, t)
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t: #found a smaller temp
                sI, sT = stack.pop()
                res[sI] = i - sI
            stack.append((i,t))
        return res