class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = defaultdict(list)

        for s in strs:
            sortedS = "".join(sorted(s))
            grp[sortedS].append(s)
        return list(grp.values())