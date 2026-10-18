class Solution:
    def clean(self, s):
        resStr = [c.lower() for c in s if c.isalnum()]

        return resStr

    def isPalindrome(self, s: str) -> bool:
        s = self.clean(s)

        return s[::] == s[::-1]