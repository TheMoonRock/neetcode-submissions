from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)

        for idx_row, row in enumerate(board):
            for idx_col, element in enumerate(row):
                if element == ".":
                    continue

                idx_box = (idx_row // 3, idx_col // 3)

                if (
                    element in cols[idx_col]
                    or element in rows[idx_row]
                    or element in boxes[idx_box]
                ):
                    return False

                cols[idx_col].add(element)
                rows[idx_row].add(element)
                boxes[idx_box].add(element)

        return True