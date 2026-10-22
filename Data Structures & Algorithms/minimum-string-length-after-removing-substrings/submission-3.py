class Solution:
    def minLength(self, s: str) -> int:
        op = list(s)

        while True:
            fd = False
            i = 0
            while i < len(op)-1:
                if op[i] == "A" and op[i+1] == "B":
                    op.pop(i)
                    op.pop(i)
                    fd = True
                elif op[i] == "C" and op[i+1] == "D":
                    op.pop(i)
                    op.pop(i)
                    fd = True

                i += 1

            if not fd:
                break

        return len(op)

            


