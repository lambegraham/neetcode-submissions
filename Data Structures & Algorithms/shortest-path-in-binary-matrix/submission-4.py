class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #start is 0,0, end is rows-1, cols-1
        rows,cols = len(grid),len(grid[0])
        #shortest path = BFS, o(V * E) V = vertexs, E = edges
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1

        visited = set([0,0])
        q = deque([(1,0,0)]) #distance, r, c

        directions=((0,1),(0,-1),(1,0),(-1,0),
                    (1,1),(1,-1),(-1,1),(-1,-1))

        while q:
                distance, cr, cc = q.popleft()
                if(cr == rows-1 and cc == cols-1):
                    return distance

                for dr, dc in directions:
                    nr = cr + dr
                    nc = cc + dc

                    if(nr<0 or nr>=rows or nc<0 or nc>=cols or
                        (nr,nc) in visited or grid[nr][nc] != 0):
                        continue

                    visited.add((nr,nc))
                    q.append((distance + 1, nr,nc))
        return -1

