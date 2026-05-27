class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inv = {}

        for i in range(len(nums)):
            cur = nums[i]
            if target - cur in inv:
                return [inv[target-cur], i]
            
            inv[cur] = i
