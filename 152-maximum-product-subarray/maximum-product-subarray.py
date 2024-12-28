class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        max_p = nums[0]
        min_p = nums[0]
        for num in nums[1:]:
            temp_max = max_p
            temp_min = min_p
            max_p = max(num,temp_max*num,temp_min*num)
            min_p = min(num,temp_max*num,temp_min*num)
            ans = max(ans,max_p)
        return ans