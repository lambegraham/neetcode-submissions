class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #valid tree:
        #1: all nodes are connected DONE
        #2: no cycles DONE
        #3: valid tree with n nodes must always have exactly n-1 edges!!! DONE
        #check edges
        if len(edges) != n-1:
            return False      
        #compute adj 
        adj = defaultdict(list)
        for u,v in edges: #u <-> v | node1 <-> node2 
            adj[u].append(v)
            adj[v].append(u)
            #[0,1],[1,2] -> {0: [1], 1: [0,2], 2: [1]}
        
        #init our vars for bfs O(V + E)
        visited = set()
        visited.add((0))
        q = deque([(0,-1)])  #0 is our start, -1 is our parent. no parent = -1 placeholder
        #q = (start, parent)

        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                #undirected! ignore
                if nei == parent:
                    continue
                #no cycles:
                if nei in visited:
                    return False
                visited.add(nei)
                q.append((nei, node)) #future node, parent it came from
        return len(visited) == n #check that we have visited all nodes 