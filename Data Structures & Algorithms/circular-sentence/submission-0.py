class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        ct = sentence.split(" ")

        for i in range(len(ct)):
            b4 = i-1
            nxt = (i+1)%(len(ct))

            if ct[b4][-1] != ct[i][0] or ct[nxt][0] != ct[i][-1]:
                return False

        return True
