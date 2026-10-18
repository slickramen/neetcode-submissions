class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1

        mVol = 0

        while l <= r:
            vol = min(heights[l], heights[r]) * (r-l)
            mVol = max(mVol, vol)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return mVol
