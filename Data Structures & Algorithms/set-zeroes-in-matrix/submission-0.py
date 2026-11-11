class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return
        row_length = len(matrix)
        col_length = len(matrix[0])
        zero_rows = set()
        zero_cols = set()
        for r in range(row_length):
            for c in range(col_length):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)
        for r in range(row_length):
            for c in range(col_length):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0