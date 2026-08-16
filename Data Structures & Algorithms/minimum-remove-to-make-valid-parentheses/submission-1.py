class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        chars = list(s)
        stack = []

        for i, c in enumerate(chars):
            if c == '(':
                stack.append(i)
            elif c == ')' and stack:
                stack.pop()
            elif c == ')' and not stack:
                chars[i] = ''
        while stack:
            chars[stack.pop()] = ''

        return "".join(chars)