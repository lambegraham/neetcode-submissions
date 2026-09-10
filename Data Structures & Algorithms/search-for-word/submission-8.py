class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #output = T OR F
        #is it nxn? or nxm? nxm = need rows & cols
        #4 directions, not 8!

        rows, cols = len(board), len(board[0])
        #directions = UDLR OR recursive
        visited = set()

        def dfs(r,c,i): #rc = rows cols, i = word[i]
            if i == len(word):
                return True 
            if(r<0 or c<0 or r>=rows or c>=cols or 
                (r,c) in visited or word[i] != board[r][c]):
                return False

            visited.add((r,c))
            #check our new directions
            res = ( dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c - 1, i + 1) or
                    dfs(r, c + 1, i + 1))
            visited.remove((r,c))
            return res

        for row in range(rows):
            for col in range(cols):
                if(dfs(row,col,0)):
                    return True
        return False