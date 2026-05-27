class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hm = {}

        for i in range(n):
            complement = target - nums[i]
            if complement in hm:
                return [hm[complement], i]
            hm[nums[i]] = i

        return []