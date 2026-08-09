class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        area = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r,c):
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            tempMaxArea = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions: #compute diff in direction
                    nr = row + dr #new row
                    nc = col + dc #new col
                    #check for out of bounds or already seen
                    if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or
                        grid[nr][nc] == 0):
                        continue
                        
                    grid[nr][nc] = 0
                    tempMaxArea+=1
                    q.append((nr,nc))
            return tempMaxArea

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    area = max(area, bfs(row,col))
        return area