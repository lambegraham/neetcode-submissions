class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # count chars
        count = defaultdict(int)
        res = 0
        l = 0
        maxf = 0 #max freq

        for r in range(len(s)):
            count[s[r]] += 1 #add max freq char
            maxf = max(maxf, count[s[r]]) #track it

            if (r - l + 1) - maxf > k: #if window length - maxf > k
                count[s[l]] -= 1 #remove l from count
                l += 1 #shrink window
            res = max(res, (r - l + 1)) #track max window
        return res