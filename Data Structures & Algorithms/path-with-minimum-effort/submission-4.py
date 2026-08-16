class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        minHeap = [[0,0,0]] #diff, r, c
        visited = set()

        while minHeap:
            diff, r, c = heapq.heappop(minHeap) #pop our dist, r, c
            if(r,c) in visited: #if visited
                continue
            visited.add((r,c)) #push to visited

            if(r == rows-1 and c == cols-1): #if final
                return diff
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                # if not OOB or visited
                if( nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    (nr, nc) in visited):     
                    continue
                
                nDiff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(minHeap, [nDiff, nr, nc])
        return 0


