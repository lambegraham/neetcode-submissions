class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(ir,ic):
            q = deque([(ir,ic)])

            while q:
                r, c = q.popleft()
                grid[r][c] = "0"

                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if(nr < 0 or nr >= ROWS or nc < 0 
                    or nc >= COLS or grid[nr][nc] == "0"):
                        continue

                    q.append((nr,nc))
                    grid[nr][nc] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        return islands
