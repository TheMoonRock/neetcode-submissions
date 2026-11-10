class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_finish_position = len(word)
        abbr_finish_position = len(abbr)
        word_ptr, abbr_ptr = 0, 0
        while word_ptr < word_finish_position and abbr_ptr < abbr_finish_position:
            # leading zeros are invalid
            if abbr[abbr_ptr] == '0':
                return False

            if word[word_ptr] == abbr[abbr_ptr]:
                word_ptr += 1
                abbr_ptr += 1
            elif abbr[abbr_ptr].isalpha():
                return False
            else:
                subLen = 0
                while abbr_ptr < abbr_finish_position and abbr[abbr_ptr].isdigit():
                    subLen = subLen * 10 + int(abbr[abbr_ptr])
                    abbr_ptr += 1
                word_ptr += subLen
            
        return word_ptr == word_finish_position and abbr_ptr == abbr_finish_position