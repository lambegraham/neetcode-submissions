class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [float('inf')] * n
        visited = [False] * n 
        node, edges, res = 0, 0, 0

        while edges < n - 1: #if n nodes, edges = n-1
            nextNode = -1 #temp nextNode
            visited[node] = True #visit current node

            for i in range(n):
                if visited[i]:
                    continue #already set it
                
                currDist = (abs(points[node][0] - points[i][0]) + abs(points[node][1] - points[i][1]))
                dist[i] = min(dist[i], currDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
                    
            res += dist[nextNode]
            node = nextNode
            edges += 1
        return res