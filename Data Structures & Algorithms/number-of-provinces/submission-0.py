class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        pCount = 0

        def dfs(node):
            visited.add(node)
            for nei in range(len(isConnected)):
                if isConnected[node][nei] and nei not in visited:
                    dfs(nei)
                    
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                pCount +=1

        return pCount