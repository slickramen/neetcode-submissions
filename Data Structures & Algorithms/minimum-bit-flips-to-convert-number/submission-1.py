class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s1 = int(bin(start), 2)
        s2 = int(bin(goal), 2)

        s3 = bin(s1^s2)

        return str(s3).count("1")
