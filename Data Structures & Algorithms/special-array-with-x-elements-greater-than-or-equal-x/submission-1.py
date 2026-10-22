class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)

        while l <= r:
            mid = (l+r)//2

            ct = 0
            for i in range(len(nums)):
                if nums[i] >= mid:
                    ct += 1

            if ct == mid:
                return ct
            elif ct < mid:
                r = mid-1
            else:
                l = mid+1

        return -1