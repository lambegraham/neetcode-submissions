class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set() #Don't want dupes, and O(1)

        def dfs(r,c,i): #i = word[i]
            if i == len(word): #base case
                return True 
            #OOB
            if(r < 0 or c < 0 or r >= rows or c >= cols
                or word[i] != board[r][c] #check if our letter is correct
                or (r, c) in path):
                return False
            #add
            path.add((r,c))
            #recursive
            res = ( dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
            #backtrack
            path.remove((r,c))
            return res

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False