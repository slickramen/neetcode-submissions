class Solution:
    def is_number(self, string):
        try:
            int(string)
            return True
        except ValueError:
            return False
    
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []

        for c in tokens:
            if self.is_number(c):
                numStack.append(int(c))
            else:
                result = 1
                if c == "+":
                    v2 = numStack.pop()
                    v1 = numStack.pop()
                    result = v1 + v2
                if c == "-":
                    v2 = numStack.pop()
                    v1 = numStack.pop()
                    result = v1 - v2
                if c == "*":
                    v2 = numStack.pop()
                    v1 = numStack.pop()
                    result = v1 * v2
                if c == "/":
                    v2 = numStack.pop()
                    v1 = numStack.pop()
                    result = v1 / v2

                numStack.append(int(result))

            print(numStack)
                
        return numStack[0]