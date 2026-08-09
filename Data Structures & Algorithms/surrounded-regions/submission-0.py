class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        #grid vars
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        rows, cols = len(grid), len(grid[0])
        #bfs vars
        q = deque()
        
        #Seed our BFS
        for row in range(rows):
            for col in range(cols):
                #queue every O on edge
                if((row == 0 or row == rows-1 or
                    col == 0 or col == cols-1) and
                    grid[row][col] == 'O'):
                        q.append((row,col))
        
        while q:
            cr, cc = q.popleft()
            if grid[cr][cc] == 'O':
                grid[cr][cc] = 'T'
                
                for dr, dc in directions:
                    nr, nc = dr + cr, dc + cc
                    if(nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols):
                        continue
                    q.append((nr,nc))
        
        for row in range(rows):
            for col in range(cols):
                #queue every O on edge
                if grid[row][col] == 'O':
                    grid[row][col] = 'X'
                elif grid[row][col] == 'T':
                    grid[row][col] = 'O'