class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #count chars
        count = defaultdict(int)
        l = 0 
        maxf = 0 #max freq char in window
        res = 0 #result INT

        for r in range(len(s)):
            count[s[r]] += 1 #add count to our char
            maxf = max(maxf, count[s[r]]) #track our max char in window

            #check if can repl K chars? 
            #if (window) - max freq > k: adjust our window
            if((r - l + 1) - maxf) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, (r-l+1))
        return res
