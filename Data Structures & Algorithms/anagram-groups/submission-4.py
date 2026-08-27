class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            sortedS = "".join(sorted(s))
            groups[sortedS].append(s)
        return list(groups.values())