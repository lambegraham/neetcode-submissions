class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bSet = {"{":"}", "(":")", "[":"]"}

        for b in s:
            if b in bSet:
                stack.append(bSet[b])
            else:
                if not stack or stack[-1] != b:
                    return False
                stack.pop()
        return stack == []