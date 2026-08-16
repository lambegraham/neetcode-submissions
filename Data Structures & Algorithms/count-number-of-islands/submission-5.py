class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = ((1,0),(-1,0),(0,1),(0,-1)) #4 directions LRUP
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            #OOB
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            #Modify in place
            grid[r][c] = "0"
            #Compute dirs
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row,col) #run dfs
                    islands += 1 #increment count
        return islands


