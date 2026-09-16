from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            store = [0] * 26
            for c in s:
                store[ord(c)-ord('a')] += 1
            res[tuple(store)].append(s)
            
        return list(res.values())

        