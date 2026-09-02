import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        prepared_string = s.translate(str.maketrans("", "", string.punctuation)).replace(" ", "").lower()
        start = 0
        length_of_string = len(prepared_string) - 1
        while start < length_of_string:
            if prepared_string[start] == prepared_string[length_of_string]:
                start += 1
                length_of_string -= 1
            else:
                return False
        return True