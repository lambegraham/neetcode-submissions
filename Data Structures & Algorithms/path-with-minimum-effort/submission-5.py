class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        minHeap = [[0,0,0]] #effort, row, col
        visited = set()

        while minHeap:
            #visited check
            diff, r, c = heapq.heappop(minHeap)
            if (r,c) in visited:
                continue
            visited.add((r, c))

            #final check
            if r == rows-1 and c == cols-1:
                return diff

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if (nr < 0 or nr >= rows
                    or nc < 0 or nc >= cols
                    or (nr,nc) in visited):
                    continue
                
                newDiff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(minHeap, (newDiff, nr, nc))
        return 0 #false case