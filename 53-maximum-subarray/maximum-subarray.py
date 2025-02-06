class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_s = float('-Inf')
        cum_sum = 0
        for num in nums:
            if cum_sum >0:
                cum_sum+=num
            else:
                cum_sum = num
            max_s = max(max_s,num,cum_sum)
        return max_s
            