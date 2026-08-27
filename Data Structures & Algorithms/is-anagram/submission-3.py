class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sd = defaultdict(int)
        td = defaultdict(int)
        for i in range(len(t)):
            sd[s[i]] += 1
            td[t[i]] += 1
        
        return sd == td