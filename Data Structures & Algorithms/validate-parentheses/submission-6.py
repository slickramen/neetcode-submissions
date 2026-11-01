class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stk = []

        for c in s:
            if c in pairs.keys():
                if stk and stk[-1] == pairs[c]:
                    stk.pop()
                else:
                    return False

            elif c in pairs.values():
                stk.append(c)

        return len(stk) == 0