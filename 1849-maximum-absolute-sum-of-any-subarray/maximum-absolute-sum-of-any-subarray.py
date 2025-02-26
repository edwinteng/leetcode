class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_s = nums[0]
        cur_sum = 0
        min_s = nums[0]
        for num in nums:
            cur_sum = max(num,cur_sum+num)
            max_s = max(max_s,cur_sum)
        cur_sum = 0
        for num in nums:
            cur_sum = min(num, cur_sum+num)
            min_s = min(cur_sum,min_s)
        return max(max_s,abs(min_s))