class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str2

        for i in range(len(str2), 0, -1):
            c = 0
            works = True

            targ, mins = str1, str2

            if len(str2) > len(str1):
                targ, mins = str2, str1

            div = mins[:i]

            while c < len(targ):
                if (c >= len(str1) or str1[c:(c+i)] == div) and (c >= len(str2) or str2[c:(c+i)] == div):
                    c += i
                else:
                    works = False
                    break

            if works:
                return div
        
        return ""