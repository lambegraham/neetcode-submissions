class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            letters1 = {}
            letters2 = {}
            for i in range(len(s)):
                letters1[s[i]] = letters1.get(s[i], 0) + 1
                letters2[t[i]] = letters2.get(t[i], 0) + 1
        else:
            return False
        return letters1 == letters2