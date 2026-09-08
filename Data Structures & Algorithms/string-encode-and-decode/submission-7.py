class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = '|'
        string = ""
        for word in strs:
            string += f"{len(word)}{delimiter}{word}"
        return string

    def decode(self, s: str) -> List[str]:
        delimiter = '|'
        result = []
        last_char_pos = 0
        string_len = len(s)

        while last_char_pos < string_len:
            num_pos = last_char_pos
            while s[num_pos] != delimiter:
                num_pos += 1
            word_len = int(s[last_char_pos:num_pos])
            word_start = num_pos + 1
            word_end = word_start + word_len
            word = s[word_start:word_end]

            result.append(word)

            last_char_pos = word_end

        return result