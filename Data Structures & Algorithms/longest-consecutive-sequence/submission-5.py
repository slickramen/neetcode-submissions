class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort = sorted(set(nums))
        maxLcs = 0
        curLcs = 1

        if len(sort) == 0:
            return 0

        last = sort[0]

        for i in range(1, len(sort)):
            if sort[i] == last+1:
                curLcs += 1
                maxLcs = max(maxLcs, curLcs)
            else:
                curLcs = 1

            last = sort[i]

        maxLcs = max(maxLcs, curLcs)
        return maxLcs

