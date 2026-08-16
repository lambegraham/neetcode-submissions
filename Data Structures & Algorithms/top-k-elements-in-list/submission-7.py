class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
        
        minHeap = [] #(freq, num)
        for num in freq.keys():
            heapq.heappush(minHeap, (freq[num], num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res