class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair: [temp, index]

        for i, t in enumerate(temperatures): #index, temp
            while stack and stack[-1][0] < t: #found a higher t
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = (i - stackIndex)
            stack.append([t,i])
        return res
