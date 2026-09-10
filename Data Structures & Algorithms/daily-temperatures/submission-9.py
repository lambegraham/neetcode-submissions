class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures) #0 in false
        stack = [] #i, t

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                sI, sT = stack.pop()
                res[sI] = (i - sI)
            stack.append((i,t))
        return res