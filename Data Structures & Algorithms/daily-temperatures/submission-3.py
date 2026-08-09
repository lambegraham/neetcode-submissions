class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) #0 = no temp found yet
        stack = [] #[(temp,index), (..)] days waiting for a warmer day
        
        for day, temp in enumerate(temperatures):
            #if today is warmer than most recent day
            while stack and temp > stack[-1][0]: #last stack temp
                stackTemp, stackIndex = stack.pop() #pop from stack
                # number of days from the previous day until today.
                result[stackIndex] = day - stackIndex
            # today might need to wait.. so append to stack
            stack.append((temp, day))
        return result