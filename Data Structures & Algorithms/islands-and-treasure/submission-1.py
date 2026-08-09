class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #Grid vars
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        rows, cols = len(grid), len(grid[0])
        #BFS vars
        visited = set()
        q = deque()

        #== Seed BFS queue ==
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    visited.add((row,col))
                    q.append((row,col))

        #== Multi Source BFS == 
        while q:
            currRow, currCol = q.popleft()
            #compute new directions
            for dr, dc in directions:
                newRow = currRow + dr
                newCol = currCol + dc
                #skip out of bounds, water or visited
                if( newRow < 0 or newRow >= rows or
                    newCol < 0 or newCol >= cols or
                    grid[newRow][newCol] == -1 or
                    (newRow, newCol) in visited):
                        continue
                #add our distances into the new grid rows
                grid[newRow][newCol] = grid[currRow][currCol] + 1
                visited.add((newRow, newCol))
                q.append((newRow, newCol))
                
