class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for s in strs:
            ana = "".join(sorted(s))
            anagrams[ana].append(s)
            
        return list(anagrams.values())
