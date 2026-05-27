class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1

        mA = 0

        while l < r:
            mA = max(mA, min(heights[l], heights[r]) * (r-l))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return mA

