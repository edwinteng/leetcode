import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.size = k
        if k >= len(nums):
          for i in range(len(nums)):
            heapq.heappush(self.heap,nums[i])
        else:
            for i in range(k):
                heapq.heappush(self.heap,nums[i])
            for i in range(k,len(nums)):
                if nums[i]>self.heap[0]:
                    heapq.heappop(self.heap)
                    heapq.heappush(self.heap,nums[i])

    def add(self, val: int) -> int:
        if self.size ==len(self.heap):
            if val > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap,val)
        else:
            heapq.heappush(self.heap,val)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)