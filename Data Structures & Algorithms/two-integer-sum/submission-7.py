class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inverse = {}

        i = 0
        for num in nums:
            if target - num in inverse:
                return [inverse[target - num], i]
            
            inverse[num] = i
            i += 1
        