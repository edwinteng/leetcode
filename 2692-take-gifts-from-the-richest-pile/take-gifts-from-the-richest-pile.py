import heapq
from math import sqrt
class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        h = []
        ans = list()
        for index,gift in enumerate(gifts):
            heapq.heappush(h,-gift)
        for _ in range(k):
            gift = heapq.heappop(h)
            heapq.heappush(h,-int(sqrt(-gift)))
            
        return -sum(h)
