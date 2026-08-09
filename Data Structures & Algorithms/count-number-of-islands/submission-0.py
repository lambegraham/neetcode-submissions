class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        islands = 0
        #land = 1
        #water = 0

        #Visit all of the connected land (grid[x][y] = "1") -> "0"
        def dfs(x,y):
            stack = []
            grid[x][y] = "0" #Set to 0 so we don't count it 2x
            stack.append((r,c))

            while stack:
                crow, ccol = stack.pop()
                for dx, dy in directions:
                    new_x = crow + dx
                    new_y = ccol + dy
                    #out of bounds
                    if (new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols
                        or grid[new_x][new_y] == "0"):
                        continue
                    stack.append((new_x, new_y))
                    grid[new_x][new_y] = "0"
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1 #track number of islands
        return islands
                
