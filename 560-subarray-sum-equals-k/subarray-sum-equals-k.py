class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {0:1}
        count=0
        cum_sum = 0
        for n in nums:
            cum_sum+=n
            if cum_sum-k in d:
                count+=d[cum_sum-k]
            d[cum_sum] = d.get(cum_sum,0)+1
        return count

