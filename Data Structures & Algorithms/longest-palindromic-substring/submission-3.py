class Solution:
    def longestPalindrome(self, s: str) -> str:
        resL = 0
        resR = 0
        resLen = 0
        #start in middle
        for i in range(len(s)):
            #odd
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resL = l
                    resR = r
                    resLen = (r - l + 1)
                l -= 1 #decrement L, increment R since expanding out
                r += 1

            #even, add 1 onto right side
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resL = l
                    resR = r
                    resLen = (r - l + 1)
                l -= 1
                r += 1
        return s[resL : resR + 1]