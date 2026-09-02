class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        #ADJ INIT
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        #HEAP INIT
        minHeap = [(weight, 0, nei) for nei, weight in adj[0]] #o(logN) push/pop
        heapq.heapify(minHeap) #(weight, src, nei)
        #VISITED INIT
        visited = set() #o(1) r/w
        visited.add(0)
        res = 0

        while minHeap:
            weight, src, node = heapq.heappop(minHeap) 
            #node is NEXT node
            if node in visited: #already seen next node, skip
                continue
            res += weight #add weight
            visited.add(node) #add to visited
            for nei, weight in adj[node]: #find next nodes
                heapq.heappush(minHeap, (weight, node, nei))

        return res if len(visited) == n else -1 #return -1 if all nodes not seen
