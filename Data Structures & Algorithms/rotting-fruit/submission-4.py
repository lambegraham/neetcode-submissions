class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = ((1,0), (-1,0), (0,1), (0,-1))
        rows, cols = len(grid), len(grid[0])
        q = deque()
        time = 0 #simulate time
        fresh = 0 #fresh fruits remaining

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row,col))
        
        while q and fresh > 0: #while still have fruit to rot
            for _ in range(len(q)): #simulate time
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc] != 1:
                        continue #we only care about fresh fruit
                    #now we have our rotten fruit not OOB
                    grid[nr][nc] = '2'
                    q.append((nr,nc))
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1