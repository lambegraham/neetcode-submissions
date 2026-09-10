class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = ((0,1),(0,-1),(1,0),(-1,0))

        minHeap = [([0,0,0])] #diff, R, C (X Y)
        visited = set()

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if((r,c) in visited):
                continue 
            visited.add((r,c)) #visited lowest edge diff

            if (r == rows-1 and c == cols-1):
                return diff

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if(nr<0 or nc<0 or nr>=rows or nc>=cols
                    or (nr,nc) in visited):
                    continue

                newDiff = abs(heights[r][c] - heights[nr][nc])
                heapq.heappush(minHeap, (max(diff, newDiff), nr, nc))
        return -1