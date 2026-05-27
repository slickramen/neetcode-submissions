class Solution:
    def trap(self, height: List[int]) -> int:
        h = max(height)
        w = len(height)

        area = 0

        for y in range(1, h + 1):
            first = -1
            last = -1
            count = 0
            for x in range(w):
                if height[x] >= y:
                    if first == -1:
                        first = x
                    last = x
                    count += 1
            
            if first != -1 and last != -1 and first != last:
                area += max(last-(first-1)-count, 0)
            
        return area

