class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            newN = sum([int(c) * int(c) for c in str(n)])

            if newN in seen:
                return False
            
            seen.add(newN)
            n = newN

        return True