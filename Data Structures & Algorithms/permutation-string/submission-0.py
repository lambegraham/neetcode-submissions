

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq = defaultdict(int)
        for s in s1:
            freq[s] +=1

        windowFreq = defaultdict(int)
        l = 0

        for r, c in enumerate(s2):
            windowFreq[c] += 1
            if r - l + 1 > len(s1): #if the window is longer than s1 
                windowFreq[s2[l]] -= 1 # SHRINK! 
                if windowFreq[s2[l]] == 0: #if empty, delete!
                    del windowFreq[s2[l]]
                l += 1 # SHRINK!
            
            if windowFreq == freq:
                return True
        return False