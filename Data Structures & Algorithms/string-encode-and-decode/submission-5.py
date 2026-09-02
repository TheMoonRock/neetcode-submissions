class Solution:
    # Метод класса для кодирования строки
    def encode(self, strs: List[str]) -> str:
        delimiter = '|' # Выбираем разделитель
        string = "" # Инициализируем новую строку в которую будем записывать 
        for word in strs: # Для слова в списке строк
            string += "{count}{delimiter}{word}".format(
                count=len(word), delimiter=delimiter, word=word
                # Современный и более популярный вариант:
                # string += f"{len(word)}{delimiter}{word}"
            )
        return string # Возвращаем закодированную строку
    # Метод класса для декодирования строки
    def decode(self, s: str) -> List[str]:
        delimiter = "|" # Снова объявляем разделитель, так как он локальная переменная
        result = [] # Инициализируем список
        last_char_pos = 0 # позиция последнего символа
        string_len = len(s) # длина строки
        # Цикл while потомуБ что for не подойдёт. В этой задаче мы проходимся не по каждому элементу, а по группам элементов 
        while last_char_pos < string_len: # пока позиция символа меньше длины строки
            num_pos = last_char_pos #позиция символа
            while s[num_pos] != delimiter: # пока символ не равен разделителю
                num_pos += 1 # прибавляем 1. То есть ищем разделитель в этом цикле
            word_len = int(s[last_char_pos:num_pos]) # делаем срез чтобы получить число сиволов слова.
            # Это также помогает нам избежать ситуации, когда разделитель есть в слове
            word_start = num_pos + 1 # пропускаем разделитель
            word_end = word_start + word_len # находим конец слова. Номер символа начала + конца
            word = s[word_start:word_end] # делаем срез, чтобы получить слово

            result.append(word) # добавляем слово в список

            last_char_pos = word_end # обновляем номер начала. Переходим к новым метаданным

        return result # возвращаем результат

    # Этот подход называют Length-Prefixing (префикс длины) или Length-Delimited Framing (фрейминг с ограничением по длине).