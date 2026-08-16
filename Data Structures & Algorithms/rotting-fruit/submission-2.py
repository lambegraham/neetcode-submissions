# [2, 0, 0]
# [2, 2, 2]
# [2, 0, 0]
# time += 1

#find all of the rotten fruit in grid
#start a search from each rotten 
#turn rotten, mark visited

class Solution:
    def orangesRotting(self, grid: List[List[int]]):
        #grid var
        rows, cols = len(grid), len(grid[0]) #3 3
        directions = ((1,0), (-1,0), (0,1), (0,-1))
        #bfs var
        q = deque()
        visited = set() #O(1)
        #special vars
        time = 0
        fresh = 0

        #Seed our BFS q
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2: #rotten
                    q.append((row,col)) 
                if grid[row][col] == 1: #fresh fruit
                    fresh += 1

        #q =(1,2) fresh = 0 time = 3
        while q and fresh > 0:
            for _ in range(len(q)): #1
                cr, cc = q.popleft() #curr row/col #1,0
                visited.add((cr,cc))
                for dr, dc in directions: #
                    nr = cr + dr #new row 
                    nc = cc + dc #new col 
                    #1,2
                    if(nr < 0 or nr >= rows or nc < 0 or nc >= cols
                        or grid[nr][nc] != 1):
                        continue
                    
                    grid[nr][nc] = 2 #(1,2) = 2
                    fresh-=1
                    q.append((nr,nc))
            #track time
            time += 1 
        return time if fresh == 0 else -1
