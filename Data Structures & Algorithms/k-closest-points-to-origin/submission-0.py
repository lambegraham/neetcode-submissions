class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points: #[[x,y],[x,y]]
            #point = [x, y]
            x = point[0]
            y = point[1]
            dist = x * x + y * y
            heapq.heappush(heap, (-dist, x, y))
        while len(heap) > k:
            heapq.heappop(heap)
        return [[x,y] for heap, x, y in heap]

