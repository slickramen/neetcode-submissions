class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        stk = defaultdict(int)

        ls = -1

        for i in range(len(s)):
            if s[i] in stk:
                ls = max(ls, i-1-stk[s[i]])
            else:    
                stk[s[i]] = i

        return ls


