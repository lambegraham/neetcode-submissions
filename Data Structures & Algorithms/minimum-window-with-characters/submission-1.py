class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        windowCount = defaultdict(int)
        targetCount = defaultdict(int)
        l = 0
        satisfied = 0
        bestWindow = float('inf')
        res = [] # (L, R)

        for c in t:
            targetCount[c] += 1
        required = len(targetCount)

        for r, c in enumerate(s):
            windowCount[s[r]] += 1

            if c in targetCount and windowCount[c] == targetCount[c]:
                satisfied += 1
                while satisfied == required:
                    if (r - l + 1) < bestWindow:
                        bestWindow = (r - l + 1)
                        res = [l, r]
                    if s[l] in targetCount and windowCount[s[l]] == targetCount[s[l]]:
                        #we will break the window by removing it
                        satisfied -= 1 
                    windowCount[s[l]] -= 1
                    l += 1
        return s[res[0] : res[1]+1] if bestWindow != float('inf') else ""
