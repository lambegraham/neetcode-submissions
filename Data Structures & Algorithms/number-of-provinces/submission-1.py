class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        pCount = 0

        def bfs(node):
            q = deque([node])
            while q:
                node = q.popleft()
                for nei in range(len(isConnected)):
                    if isConnected[node][nei] and nei not in visited:
                        visited.add(node)
                        q.append(nei)

        for city in range(len(isConnected)):
            if city not in visited:
                bfs(city)
                pCount +=1

        return pCount