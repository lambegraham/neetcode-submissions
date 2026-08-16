class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        rows, cols = len(grid), len(grid[0])

        def bfs(ir,ic):
            q = deque([(ir,ic)])
            grid[ir][ic] == "0"

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if(nr<0 or nc<0 or nr>=rows or nc>=cols
                        or grid[nr][nc] == "0"):
                        continue
                    
                    grid[nr][nc] = "0"
                    q.append((nr,nc))
                    
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    bfs(row,col)
        return islands