class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        ans = 0
        max_p=nums[0]
        cum_max=nums[0]
        cum_min = nums[0]
        for num in nums[1:]:
            temp_max,temp_min = cum_max,cum_min
            cum_max=max(num,temp_max*num,temp_min*num)
            cum_min=min(num,temp_min*num,temp_max*num)
            max_p = max(max_p,cum_max)
        return max_p

            
