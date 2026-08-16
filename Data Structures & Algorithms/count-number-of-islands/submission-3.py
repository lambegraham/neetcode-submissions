class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r,c):
            q = deque()
            grid[r][c] = '0' #mark start cell visited
            q.append((r,c))

            while q:
                cr, cc = q.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if(nr < 0 or nr >= rows or nc < 0 or nc >= cols
                        or grid[nr][nc] == '0'):
                        continue
                    #else
                    grid[nr][nc] = '0'
                    q.append((nr,nc))
                    
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    bfs(row,col)
                    islands += 1
        return islands