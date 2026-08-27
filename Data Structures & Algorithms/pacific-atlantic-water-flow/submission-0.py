class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        directions = ((1,0), (-1,0), (0,1), (0,-1))
        rows, cols = len(heights), len(heights[0])

 
        def bfs(collection):
            q = deque(collection)
            res = set()
            visited = set(collection)
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols
                        or (nr,nc) in visited 
                        or heights[nr][nc] < heights[r][c]):
                        continue
                    visited.add((nr,nc))
                    q.append((nr,nc))
            return visited

        pacific = set()
        atlantic = set()
        for row in range(rows):
            for col in range(cols):
                if (row == 0 or col == 0): #pacific
                    pacific.add((row,col))
                if (row == rows-1 or col == cols-1 ): #atlantic
                    atlantic.add((row,col))

        answerpacific = bfs(pacific)
        answeratlantic = bfs(atlantic)

        return list(answerpacific & answeratlantic)
