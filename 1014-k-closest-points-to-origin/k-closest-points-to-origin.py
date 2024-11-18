import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        ans = []
        for point in points:
            x,y = point
            heapq.heappush(h,[x*x+y*y,point])
        for i in range(k):
            distance,point = heapq.heappop(h)
            ans.append(point)
        return ans
