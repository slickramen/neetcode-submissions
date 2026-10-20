class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [False for _ in range(n)]

        for ai, bi in trust:
            trusts[ai-1] = True

        cand = []

        for i in range(n):
            if not trusts[i]:
                cand.append(i)

        newCand = []
        for c in cand:
            trustedBy = 0

            for ai, bi in trust:
                if bi == c+1:
                    trustedBy += 1

            if trustedBy == n-1:
                newCand.append(c+1)
            

        if len(newCand) == 1:
            return newCand[0]

        return -1

