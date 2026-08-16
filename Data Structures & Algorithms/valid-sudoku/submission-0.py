class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                
                if (board[r][c] in rows[r] or #if already found in rows
                    board[r][c] in cols[c] or #or cols
                    board[r][c] in squares[(r//3, c//3)]): #or squares
                    return False

                #add it to the sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True