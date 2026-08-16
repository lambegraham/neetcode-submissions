class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        while l < r:
            totalTime = 0
            mid = (r + l) // 2 #attempt of k
            for p in piles:
                totalTime += (math.ceil(p / mid))
            if totalTime <= h: #speed too fast, try smaller k, discard right
                r = mid
            elif totalTime > h: #result is too slow, go faster
                l = mid + 1
            
        return l

        #h = limit of hours we have to eat all
        #k = the banana per hour eating rate
        #find minimum k such that we eat all within h