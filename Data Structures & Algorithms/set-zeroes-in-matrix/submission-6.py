class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        if not matrix or not matrix[0]:
            return
        
        first_row_contain_zeros = False
        first_col_contain_zeros = False

        row_len = len(matrix)
        col_len = len(matrix[0])

        for c in range(col_len):
            if matrix[0][c] == 0:
                first_row_contain_zeros = True
                break
        
        for r in range(row_len):
            if matrix[r][0] == 0:
                first_col_contain_zeros = True
                break
        
        for r in range(1, row_len):
            for c in range(1, col_len):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, row_len):
            for c in range(1, col_len):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_row_contain_zeros:
            for c in range(col_len):
                matrix[0][c] = 0
        
        if first_col_contain_zeros:
            for r in range(row_len):
                matrix[r][0] = 0