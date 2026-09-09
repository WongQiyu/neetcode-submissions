from heapq import heappop, heappush, heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        store = []
        res = []
        heapify(store)
        for p in points:
            dist = (p[0]-0) **2 + (p[1]-0) **2
            heappush(store,(dist,p))

        for _ in range(k):
            _,point = heappop(store)
            res.append(point)
        
        return res
        

        