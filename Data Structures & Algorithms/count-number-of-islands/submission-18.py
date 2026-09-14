#mock interview
#2d grid, land water, if they touch h or v they are connected, return total num of islands 
#grid m * n, land = 1, water = 0, return total num of islands in this grid
#[1, 0]
#[0, 1]
#directions UDLR, bfs/dfs, find a island, q into bfs/dfs, mark each visited / 0, 
#time = O(m * n) m = rows n = cols
#space = O(m * n)
#grid single cell [1]

class Solution:
    def numIslands(self, grid):
        #change in place 
        directions = ((1,0), (-1,0), (0,1), (0,-1)) #4D
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(ri, ci): #row in, col in
            q = deque([(ri,ci)]) #start with our ri,ci
            while q:
                r, c = q.popleft() #current row & col
                grid[r][c] = '0' #mark visited
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c #new row, new col
                    if nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc] == '0':
                        continue
                    #not OOB, is land
                    q.append((nr,nc))
                    grid[nr][nc] = '0' #mark at enqueue time to prevent duplicates
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    bfs(row,col) #BFS in: [0,0] [1,1]
                    islands += 1 #2
        return islands