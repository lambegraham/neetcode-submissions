class MedianFinder:
    def __init__(self):
        self.small = [] #maxheap -
        self.large = [] #minheap +

    def addNum(self, num: int) -> None:
        #if large exists and num is bigger than smallest large
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num) #add to large
        else:
            heapq.heappush(self.small, -num) #add to small
    
        #check lens, if diff is > 1:
        if abs(len(self.large) - len(self.small)) > 1:
            if len(self.large) > len(self.small): #if large bigger
                t = heapq.heappop(self.large) #pop large
                heapq.heappush(self.small, -t) #add to small-
            elif len(self.small) > len(self.large): #if small bigger
                t = -heapq.heappop(self.small) #pop -small
                heapq.heappush(self.large, t) #add to large
            
    def findMedian(self) -> float: #bigger heap has median
        if len(self.large) > len(self.small):
            return self.large[0]
        if len(self.small) > len(self.large):
            return -self.small[0]
        else: #equal, do math
            return ((-self.small[0] + self.large[0]) / 2)
        