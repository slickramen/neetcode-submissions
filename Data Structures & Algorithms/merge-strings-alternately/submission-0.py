class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        idx = 0
        while idx < len(word1) and idx < len(word2):
            if len(res) % 2 == 0:
                res += word1[idx]
            else:
                res += word2[idx]
                idx += 1


        res += word1[idx:]
        res += word2[idx:]

        return res