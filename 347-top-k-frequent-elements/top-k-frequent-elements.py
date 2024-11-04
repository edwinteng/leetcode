import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        h = []
        ans = list()
        for key in d.keys():
            heapq.heappush(h,(-d[key],key))
        for i in range(k):
            freq,element = heapq.heappop(h)
            ans.append(element)
        return ans
