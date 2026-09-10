class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures) #0 in false
        stack = [] #i, t

        for i, t in enumerate(temperatures):
            while stack:
                if t > stack[-1][1]: #found bigger temp
                    sI, sT = stack.pop()
                    res[sI] = (i - sI)
                else:
                    break
            stack.append((i,t))
        return res