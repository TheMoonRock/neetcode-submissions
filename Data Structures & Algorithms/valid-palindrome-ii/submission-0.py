class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if self.check(s, left+1, right) or self.check(s, left, right-1):
                    return True
                else:
                    return False
        return True

    def check(self, s, left, right):
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True