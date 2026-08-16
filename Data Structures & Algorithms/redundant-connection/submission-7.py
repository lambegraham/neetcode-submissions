class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        degree = defaultdict(int)
        n = len(edges)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1

        q = deque()
        #check for 1 degrees
        for i in range(1, n+1):
            if degree[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()
            degree[node] -= 1
            #remove degree from nei nodes
            for nei in adj[node]:
                degree[nei] -= 1
            #if now a leaf, remove it too
            if degree[nei] == 1:
                q.append(nei)
        for u, v in reversed(edges):
            if degree[u] > 0 and degree[v] > 0:
                return [u,v]
        return []

