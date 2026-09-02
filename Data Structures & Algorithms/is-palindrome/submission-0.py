class Solution:
    def isPalindrome(self, s: str) -> bool:
        m = s.lower()
        cleaned_text = "".join(char for char in m if char.isalnum() or char.isspace())
        d = cleaned_text.replace(" ", "")
        print(d)
        print(d[::-1])
        return d == d[::-1]