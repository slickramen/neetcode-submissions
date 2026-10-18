class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 1:
            return 0

        order = [int(s[0]), 1-int(s[0])]

        return min(
            sum([abs(int(s[i])-order[i%2]) for i in range(len(s))]),
            sum([abs(int(s[i])-order[(1 + i)%2]) for i in range(len(s))])
        )