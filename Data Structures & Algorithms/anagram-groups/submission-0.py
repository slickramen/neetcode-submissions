class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            k = "".join(sorted(s))
            ans[k].append(s)

        return list(ans.values())