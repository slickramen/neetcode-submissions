class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        shortest = min(strs, key=len)

        for i in range(len(shortest)):
            target = shortest[i]

            for s in strs:
                if s[i] != target:
                    return pref
            
            pref += target

        return pref

