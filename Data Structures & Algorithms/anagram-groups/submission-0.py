class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ["act","pots","tops","cat","stop","hat"]
        groups = {}
        for w in strs:
            ss = "".join(sorted(w))
            groups[ss] = groups.get(ss, []) + [w]
        return list(groups.values())