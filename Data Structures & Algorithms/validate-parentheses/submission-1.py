class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closes = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in closes:
                if stack and stack[-1] == closes[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0

