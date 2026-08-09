class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #Grid vars
        rows, cols = len(grid), len(grid[0])
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        #BFS vars
        visited = set()
        q = deque()

        #== Seed BFS queue ==
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0: #treasure chest found
                    q.append((row,col))
                    visited.add((row,col))

        #== Multi Source BFS == 
        while q:
            cr, cc = q.popleft() 
            for dr, dc in directions:
                nr = cr + dr
                nc = cc + dc

                if(nr < 0 or nr >= rows or nc < 0 or nc >= cols 
                or (nr,nc) in visited or grid[nr][nc] == -1):
                    continue
                
                grid[nr][nc] = grid[cr][cc] + 1
                visited.add((nr,nc))
                q.append((nr,nc))


                
