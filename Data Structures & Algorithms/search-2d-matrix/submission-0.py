class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, ROWS * COLS - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // COLS
            col = mid % COLS

            if matrix[row][col] > target: #too big, search left
                right = mid - 1
            elif matrix[row][col] < target: #too small, search right
                left = mid + 1
            else:
                return True
        return False