class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ppl = []

        for i in range(len(names)):
            ppl.append((names[i], heights[i]))

        return ([name for name, score in sorted(ppl, key=lambda x: x[1], reverse=True)])