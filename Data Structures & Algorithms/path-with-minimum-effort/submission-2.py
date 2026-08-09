class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = ((0,1),(0,-1),(1,0),(-1,0))
       
        def bfs(threshold):
            q = deque([(0,0)])
            visited = {(0,0)}

            while q:
                r, c = q.popleft() #pop our r, c
                #if final
                if(r == rows-1 and c == cols-1):
                    return True

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    # if not OOB
                    if( nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols):     
                        continue
                    # if not visited and <= threshold
                    if( (nr,nc) not in visited and
                        abs(heights[nr][nc]-heights[r][c]) <= threshold):
                        visited.add((nr,nc))
                        q.append((nr,nc))
            return False

        #binary search
        l = 0
        #max effort? abs diff between all heights
        r = max(map(max, heights)) - min(map(min, heights))
        
        while l < r:
            mid = (l + r) // 2
            if bfs(mid): #can reach, in left half, discard right
                r = mid
            else:   #cant reach, in right of mid, discard left
                l = mid + 1 
        return l



