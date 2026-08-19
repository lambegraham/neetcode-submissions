class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)

        while l < r:
            time = 0
            mid = (l + r) // 2

            for p in piles:
                time += math.ceil(p / mid)

            if time > h: #too slow, speed up, make mid bigger
                l = mid + 1
            if time <= h: #too fast, make mid smaller
                r = mid
        return l
