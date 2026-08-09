class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)
            # print(heap[0])
        while len(heap) > 1:
            s1 = -heapq.heappop(heap) #always heavier!
            s2 = -heapq.heappop(heap)
            if s1 != s2:
                heapq.heappush(heap, -(s1 - s2))
        return -heap[0] if heap else 0