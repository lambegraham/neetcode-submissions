class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Grid vars
        rows, cols = len(grid), len(grid[0])
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        #BFS vars - lvl by lvl = each level 1 unit of time BFS O(m * n)
        q = deque()
        visited = set() #O(1)
        fresh = 0
        time = 0

        #=== Seed our BFS ===
        #in: grid
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row,col)) #rotten fruit!
                if grid[row][col] == 1:
                    fresh += 1 #fresh fruit
        #out: fresh & rotten fruit

        #=== BFS ===
        #in: queue of the rotten fruits
        while q and fresh > 0:
            for _ in range(len(q)):
                cr, cc = q.popleft() #current row and col
                for dr, dc in directions:
                    nr = cr + dr #nr = new row
                    nc = cc + dc #nc = new col

                    #out of bounds M * N = edge = out of bounds
                    if(nr < 0 or nr >= rows or nc < 0 or nc >= cols
                    or grid[nr][nc] != 1):
                        continue
                    #rot the fruit
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            time+=1
        #out: time to rot all fresh fruits DONE
        return time if fresh == 0 else -1

