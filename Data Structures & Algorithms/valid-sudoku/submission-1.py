class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set) # словарь множеств колонок
        rows = defaultdict(set) # словарь множеств строк
        squares = defaultdict(set) # словарь множеств квадратов 3 на 3 путём деленния чисел на три без остатка

        for r in range(9): # перебираем строки
            for c in range(9): # перебираем колонки
                if board[r][c] == ".":
                    continue # пропускаем пустые значения
                if ( board[r][c] in rows[r] # проверяем существует ли элемент в словаре множеств, где ключ это номер строки, а значение множество уже добавленных элементов в этой строке.
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                # В этом блоке мы добавляем данные
                cols[c].add(board[r][c]) # Например добавляем в словарь колонок под номер колонки (ключ словаря) элемент в множество соответсвующее элементам этой колонки. 
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True