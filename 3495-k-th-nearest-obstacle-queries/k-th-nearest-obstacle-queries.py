import heapq
class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        h = []
        ans = []
        for i in range(len(queries)):
            d = abs(queries[i][0])+abs(queries[i][1])
            heapq.heappush(h,-d)
            if i>=k:
                heapq.heappop(h)
            if i>=k-1:
                ans.append(-h[0])
            else:
                ans.append(-1)
        return ans
