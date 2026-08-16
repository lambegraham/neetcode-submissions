class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal = ""
        longest = 0

        for i in range(len(s)):

            l = r = i
            #odd len palin
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #check if longer
                if r - l + 1 > longest:
                    longest = r - l + 1
                    pal = s[l:r+1]
                l -=1 
                r +=1 

            #even len 
            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > longest:
                    longest = r - l + 1
                    pal = s[l:r+1]
                l -= 1
                r += 1

        return pal