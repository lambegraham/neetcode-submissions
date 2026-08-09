class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        s = str(x)
        s1 = ""
        for i in range(len(s)-1, -1, -1):
            s1  += s[i]
        return x == int(s1)
            