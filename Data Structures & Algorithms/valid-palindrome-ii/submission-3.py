class Solution:
    def pal(self, s):
        return s[::-1] == s[:]
    def validPalindrome(self, s: str) -> bool:
        if self.pal(s):
            return True
        for i in range(len(s)+1):
            cs = s[:i-1] + s[i:]
            if self.pal(cs):
                return True
        return False