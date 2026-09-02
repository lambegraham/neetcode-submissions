class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)
        for u, v, cost in flights:
            adj[u].append((v,cost))

        minHeap = [(0, src, -1)] #cost, node, stops
        visited = set() #track airports already visited?

        while minHeap:
            cost, node, stops = heapq.heappop(minHeap)
            state = (node, stops)
            
            if state in visited or stops > k: #check if visited already or above stops
                continue
            visited.add(state)

            if node == dst: #check if reached
                return cost

            for nei, price in adj[node]: #check next airports
                heapq.heappush(minHeap, (cost+price, nei, stops + 1))
            
        return -1