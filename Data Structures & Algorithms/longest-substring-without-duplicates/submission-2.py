class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
            
        seen = set(s[0])
        l = 0
        r = 1

        max_sub = 1

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                seen.remove(s[l])
                l += 1

            max_sub = max(max_sub, r-l)

        return max_sub