class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ns, ne =  newInterval[0], newInterval[1]
        res = []
        added = False

        for s, e in intervals:
            if ns > e:
                res.append([s,e])
            elif ne < s:
                if not added:
                    res.append([ns,ne])
                    added = True
                res.append([s,e])
            else:
                ns = min(s,ns)
                ne = max(e,ne)
        if not added:
            res.append([ns,ne])
        return res
        
        
        