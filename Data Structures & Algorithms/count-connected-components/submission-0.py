class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        visit = [False] * n #init visited set of False
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(node):
            q = deque([node])
            visit[node] = True

            while q:
                n = q.popleft()
                for nei in adj[n]:
                    if visit[nei] == False: #check we have not visited, visit
                        visit[nei] = True #mark visited
                        q.append(nei) #continue searching from there
        
        res = 0 
        for node in range(n): #go through all nodes
            if visit[node] == False: #if not visited, visit
                bfs(node)
                res += 1
        return res
            