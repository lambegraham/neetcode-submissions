class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)): #nested loop to calc 2 points
            x1, y1 = points[i]
            for j in range(i+1, len(points)): #remember this i+1 !
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append((dist,j)) #normal adj
                adj[j].append((dist,i)) #undirected
        
        visited = set()
        minHeap = [(0,0)] #cost, node
        res = 0

        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visited: #visited check
                continue

            visited.add(node) #visit & process
            res += cost

            for neiCost, nei in adj[node]: #check nei's
                if nei not in visited:
                    heapq.heappush(minHeap, (neiCost, nei))
        return res
            