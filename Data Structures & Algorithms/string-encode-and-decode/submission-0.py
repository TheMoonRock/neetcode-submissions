class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = "#"
        string = ""
        for word in strs:
            string += "{count}{delimiter}{word}".format(
                count=len(word), delimiter=delimiter, word=word
            ) 
        return string
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res