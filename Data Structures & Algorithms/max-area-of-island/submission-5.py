class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = ((1,0),(-1,0),(0,1),(0,-1))

        def bfs(row,col):
            q = deque([(row,col)])
            tempArea = 1
            grid[row][col] = 0

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if (nr < 0 or nr >= rows or nc < 0 or nc >= cols
                        or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 0
                    tempArea += 1
                    q.append((nr,nc))

            return tempArea

        area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = max(area, bfs(row,col))
        return area
            