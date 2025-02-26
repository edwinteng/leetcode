class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_s = nums[0]
        cur_sum_min,cur_sum_max = 0,0
        min_s = nums[0]
        for num in nums:
            cur_sum_max = max(num,cur_sum_max+num)
            max_s = max(max_s,cur_sum_max)
        
            cur_sum_min = min(num, cur_sum_min+num)
            min_s = min(cur_sum_min,min_s)
        return max(max_s,abs(min_s))