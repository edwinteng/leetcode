class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub_sum = nums[0]
        total = nums[0]
        for i in range(1,len(nums)):
            
            if total < 0:
                total = 0
            total+=nums[i]
            sub_sum=max(sub_sum,total)
        return sub_sum