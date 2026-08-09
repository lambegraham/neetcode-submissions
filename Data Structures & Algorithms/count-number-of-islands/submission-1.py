class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        islands = 0

        def bfs(r,c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newRow, newCol = dr+row, dc+col
                    #check if out of bounds
                    if (newRow < 0 or newCol < 0 or newRow >= rows or newCol >= cols 
                    or grid[newRow][newCol] == "0"):
                        continue
                    grid[newRow][newCol] = "0"
                    q.append((newRow, newCol))
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row,col)
                    islands+=1
        return islands
            
