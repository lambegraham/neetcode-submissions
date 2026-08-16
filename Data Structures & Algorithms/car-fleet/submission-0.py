class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [] #pos, time
        for i in range(len(position)):
            pair.append((position[i],speed[i]))
        stack = []

        for p, s in sorted(pair)[::-1]: #reverse sort the pairs
            stack.append((target - p) / s) #target-pos / speed = time to target
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
