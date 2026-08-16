class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #temp > most recent stack temp
                stackT, stackI = stack.pop() #pop our stack items
                res[stackI] = (i - stackI) #calc how many days
            stack.append([t, i]) #append on temp, index
        return res