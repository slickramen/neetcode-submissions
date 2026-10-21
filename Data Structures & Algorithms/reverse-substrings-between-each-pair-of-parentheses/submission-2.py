class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        res = ""
        for n in s:
            if  n != ")":
                stk.append(n)
            elif n == ")":
                op = ""
                while stk[-1] != "(":
                    op += stk.pop()
                stk.pop()
                stk.extend(op)

        res = "".join(stk)

        return res

