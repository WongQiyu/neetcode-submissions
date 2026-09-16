from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            keys = ''.join(sorted(s))
            res[keys].append(s)
        return list(res.values())

        