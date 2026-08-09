class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bSet = {"{":"}", "(":")", "[":"]"}

        for b in s:
            if b in bSet: #We saw opening bracket
                stack.append(bSet[b]) #Append closing bracket
            else: #We saw a CLOSING bracket
                if not stack or stack[-1] != b: #stack empty or last bracket does not match
                    return False
                stack.pop() #It matched, so remove CLOSING 
        return stack == []