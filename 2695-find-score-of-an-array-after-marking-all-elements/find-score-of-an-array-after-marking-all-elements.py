import heapq
class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = []
        mark = set()
        score = 0
        for index,num in enumerate(nums):
            heapq.heappush(h,(num,index))
        while len(mark) <= len(nums) and h:
            num,index = heapq.heappop(h)
            while index in mark and h:
                num,index = heapq.heappop(h)
            if index-1>=0:
                mark.add(index-1)
            if index+1<len(nums):
                mark.add(index+1)

            if index not in mark:
                mark.add(index)
                score+=num
        return score
