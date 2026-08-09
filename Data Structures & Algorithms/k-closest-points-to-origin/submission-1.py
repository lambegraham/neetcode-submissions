class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points: #[[x,y],[x,y]]
            #point = [x, y]
            x = point[0]
            y = point[1]
            dist = x * x + y * y
            heapq.heappush(heap, (-dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)

        return [(x,y) for _, x, y in heap]

