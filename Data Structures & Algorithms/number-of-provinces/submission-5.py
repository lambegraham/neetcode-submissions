class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0
        
        def dfs(node):
            visited.add(node)

            for nei in range(len(isConnected)):
                if isConnected[node][nei] and nei not in visited:
                    dfs(nei)

        for node in range(len(isConnected)):
            if node not in visited:
                count += 1
                dfs(node)
        
        return count

