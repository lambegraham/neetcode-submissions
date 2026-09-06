class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #n x n same length as width
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1: return -1

        directions = ((1,0),(-1,0),(0,1),(0,-1),
                        (1,1),(-1,1),(-1,-1),(1,-1))
        
        q = deque([(1,0,0)]) #dist, r, c
        visited = {(0,0)}

        while q: 
            dist, r, c = q.popleft()
            if (r == n-1 and c == n-1):
                return dist

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if(nr<0 or nc<0 or nr>=n or nc>=n or 
                    grid[nr][nc] == 1 or (nr,nc) in visited):
                    continue
                
                q.append((dist+1, nr, nc))
                visited.add((nr,nc))
        return -1