class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        nums.sort()

        for i in range(len(nums)):
            cur = i
            cur_length = 1
            for j in range(i + 1, len(nums)):
                if nums[j] == nums[cur] + 1:
                    cur = j
                    cur_length += 1
            
            if cur_length > longest:
                longest = cur_length

        return longest