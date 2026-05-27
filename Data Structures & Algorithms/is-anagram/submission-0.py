class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = set(s)
        lt = set(t)

        if ls != lt:
            return False
        
        for char in ls:
            if s.count(char) != t.count(char):
                return False
        return True