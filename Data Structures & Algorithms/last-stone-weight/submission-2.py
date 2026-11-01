class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while stones and len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            if s1 == s2:
                continue
            else:
                heapq.heappush(stones, s1 - s2)

        if stones:
            return -heapq.heappop(stones)
        else:
            return 0


