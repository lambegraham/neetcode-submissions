class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points) #number of points
        dist = [float("inf")] * n #min distance, use infin as starting
        visited = [False] * n #have we visited it
        edges, res, node = 0, 0, 0

        while edges < n - 1: #n - 1 is max amount of edges, 7 nodes 6 edges
            visited[node] = True
            nextNode = -1 #temp

            for i in range(n):
                if visited[i]: #if visited skip
                    continue

                #calculate distance btwn points
                curDist = (abs(points[node][0] - points[i][0]) + 
                            abs(points[node][1] - points[i][1]))
                dist[i] = min(curDist, dist[i])

                #handle first node, handle smaller distance
                if nextNode == -1 or dist[i] < dist[nextNode]: 
                    nextNode = i #smallest distance!!
            #once for loop finishes
            res += dist[nextNode]
            node = nextNode
            edges += 1 #track how many edges we have calculated
        return res