class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        l = 0
        r = 0

        subs = 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            
            subs = max(subs, len(seen))
        
        return subs