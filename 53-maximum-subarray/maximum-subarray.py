class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_s = float('-Inf')
        cum_sum = 0
        for num in nums:
            cum_sum = max(cum_sum+num,num)
            max_s = max(max_s,cum_sum)
        return max_s
            