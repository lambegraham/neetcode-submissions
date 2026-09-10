class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #output = T OR F
        #is it nxn? or nxm? nxm = need rows & cols
        #4 directions, not 8!

        rows, cols = len(board), len(board[0])
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        stack = [] #r, c, i, visited


        for row in range(rows):
            for col in range(cols):
                if(board[row][col] == word[0]):
                    stack.append((row,col,0,{(row,col)}))

        while stack:
            r, c, i, visited = stack.pop()

            if i == len(word) - 1:
                return True 

            visited.add((r,c))
            #check our new directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if(nr<0 or nc<0 or nr>=rows or nc>=cols or 
                (nr,nc) in visited or word[i+1] != board[nr][nc]):
                    continue
                newVisited = visited.copy()
                newVisited.add((nr,nc))
                stack.append((nr,nc, i+1, newVisited))
        return False