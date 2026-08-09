class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = ((0,1),(0,-1),(1,0),(-1,0)) #UDRL

        #top left to bottom right = 0,0 -> rows-1, cols-1 in ? effort
        def bfs(threshold):
            q = deque([(0,0)])
            visited = {(0,0)}
            while q:
                x, y = q.popleft() #0,0
                #end reached?
                if x == rows-1 and y == cols-1:
                    return True
                for dx, dy in directions: #our new position
                    new_x = x + dx
                    new_y = y + dy
                    #out of bounds??? less than 0, >= rows,cols
                    if (new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols):
                        continue
                    #effort? difference height between initial pos, new pos
                    #not visited!
                    #can we reach it?
                    if((new_x, new_y) not in visited and 
                        abs(heights[new_x][new_y] - heights[x][y]) <= threshold):
                        visited.add((new_x,new_y))
                        q.append((new_x,new_y))
            return False
        
        # == Binary Search ==
        #midpoint ? upper and lower bounds
        left = 0 #no effort 
        #right = range of our effort
        right = max(map(max, heights)) - min(map(min, heights))

        while left<right:
            mid = (left + right) //2
            if bfs(mid) == True: #answer is in left of mid, discard right
                right = mid
            else:
                left = mid + 1
        return left #our mininmum effort

