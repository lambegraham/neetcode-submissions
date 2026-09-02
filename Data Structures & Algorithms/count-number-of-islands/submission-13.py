class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = ((0,1),(0,-1),(1,0),(-1,0)) #simulate UPLR
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set() #track visited islands ((r,c))
        
        def bfs(rowIn, colIn):

            q = deque([(rowIn, colIn)]) #que our BFS nodes ((r,c))
            visited.add((rowIn,colIn))

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if(nr < 0 or nr >= rows or nc < 0 or nc >= cols
                        or (nr,nc) in visited or grid[nr][nc] == '0'):
                        continue

                    q.append((nr,nc))
                    visited.add((nr,nc))
                
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row,col) not in visited:
                    bfs(row,col)
                    islands += 1
        return islands