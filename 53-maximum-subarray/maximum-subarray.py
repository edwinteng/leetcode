class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_s = nums[0]
        s = nums[0]
        for i in range(1,len(nums)):
            #start new or add new
            
            if s <0:
                s = 0
            s+=nums[i]
            max_s = max(max_s,s)
        return max_s 