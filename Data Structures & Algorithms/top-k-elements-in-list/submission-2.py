class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dd = defaultdict(int)

        for n in nums:
            dd[n] += 1

        return sorted(dd, key=dd.get, reverse=True)[:k]

        