class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v,w))
            #times = [[1,2,1], [2,3,1], [1,4,4], [3,4,1]]
            #adj = {1: [(2, 1), (4, 4)], 2: [(3, 1)], 3: [(4, 1)]}
        
        minHeap = [(0,k)] #sort by the smallest first value in minHeap
        visited = set()
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap) #weight, node
            if n1 in visited: #if visited, continue
                continue
            visited.add(n1) #else add it to visited
            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visited) == n else -1
