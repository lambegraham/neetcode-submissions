class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = [] #val, index
        res = []

        for i, num in enumerate(nums):
            heapq.heappush(maxHeap, (-num, i))
            while maxHeap[0][1] <= i - k: #pop out of range
                heapq.heappop(maxHeap)
            
            if i >= k - 1:
                res.append(-maxHeap[0][0])
        return res