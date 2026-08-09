class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        if abs(len(self.large) - len(self.small)) > 1:
            if len(self.large) > len(self.small):
                t = heapq.heappop(self.large)
                heapq.heappush(self.small, -t)
            elif len(self.small) > len(self.large):
                t = -heapq.heappop(self.small)
                heapq.heappush(self.large, t)
            
    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return ((-self.small[0] + self.large[0]) / 2)
        