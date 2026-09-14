class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = ((1,0),(-1,0),(0,1),(0,-1))

        def bfs(time): #time = water level, time 3 = water 3
            if grid[0][0] > time: #cant start at 0,0 if it is submerged
                return False
                
            q = deque([(0,0)])
            visited = {(0,0)} #set of 0,0

            while q:
                r, c = q.popleft()
                visited.add((r,c))

                if r == rows-1 and c == cols-1:
                    return True

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if nr<0 or nc<0 or nr>=rows or nc>=cols or (nr,nc) in visited or grid[nr][nc] > time:
                        continue
                    
                    #we know now not OOB and can swim here
                    visited.add((nr,nc))
                    q.append((nr,nc))
            return False
        #binary search = if level 5 true, anything anove level 5 is true
        #binary search is log n, efficient
        l = 0
        r = max(map(max,grid))#max of all cells?
        while l<r:
            mid = (l + r) // 2
            if bfs(mid): #we can reach it, search left
                res = mid
                r = mid
            else:
                l = mid + 1
        return l