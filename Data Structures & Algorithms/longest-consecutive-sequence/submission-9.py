class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        mc = 1

        if len(nums) == 0:
            return 0

        last = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == last+1:
                count += 1
            elif nums[i] == last:
                continue
            else:
                count = 1

            last = nums[i]
            mc = max(mc, count)

        return mc