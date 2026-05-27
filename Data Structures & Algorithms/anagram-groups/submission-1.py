class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each str and store in hm as that
        hm = defaultdict(list)

        for s in strs:
            cs = ''.join(sorted(s))

            hm[cs].append(s)

        return list(hm.values())