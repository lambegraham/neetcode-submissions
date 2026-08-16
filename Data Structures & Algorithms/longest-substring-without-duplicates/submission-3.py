class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #s = "zxyzxyz" = 3
        #s = "" = 0
        #s = "xxxx" = 1
        #a = "abba" = 2
        seen = set()
        l = 0
        res = 0

        for r in range(len(s)): #3, abba
            while s[r] in seen: 
                seen.remove(s[l]) #remove a
                l += 1 #2
            seen.add(s[r]) #seen = b,a
            res = max(res, r-l + 1) #2 , 3-2+1 = 2
        return res