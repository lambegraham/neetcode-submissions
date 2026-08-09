class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bSet = {"{":"}", "(":")", "[":"]"}

        for b in s:
            if b in bSet: #we saw opening bracket
                stack.append(bSet[b]) #append closing to stack
            else:
                if not stack or stack[-1] != b: #if empty or not matching
                    return False
                stack.pop()
        return stack == []