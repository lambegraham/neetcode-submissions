class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        visited = set()

        def dfs(node):
            visited.add(node)

            for nei in range(len(isConnected)):
                if isConnected[node][nei] and nei not in visited:
                    dfs(nei)
        
        for node in range(len(isConnected)):
            if node not in visited:
                dfs(node)
                count += 1
        
        return count
            