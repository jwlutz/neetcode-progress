import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for i in range(len(points)):
            points[i].append(-(points[i][0]**2 + points[i][1]**2))
        for i in range(len(points)):
            heapq.heappush(res, (points[i][2], points[i]))
            if len(res) > k:
                heapq.heappop(res)

        return [item[1][:2] for item in res]
        
            
