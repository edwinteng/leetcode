class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prd = 1
        left = 0
        count = 0
        for right in range(len(nums)):
            prd*=nums[right]
            while prd >= k and left<=right:
                prd=prd/nums[left]
                left+=1
            count+=(right-left+1)
        return count
