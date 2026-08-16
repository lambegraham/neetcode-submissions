class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        chars = list(s)
        bal = 0

        for i in range(len(s)):
            if chars[i] == '(':
                bal += 1
            elif chars[i] == ')' and bal > 0:
                bal -= 1
            elif chars[i] == ')':
                chars[i] = ''
        
        for i in range(len(s)-1, -1, -1):
            if chars[i] == '(' and bal > 0:
                bal -= 1
                chars[i] = ''

        return "".join(chars)