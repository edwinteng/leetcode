class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        i = 0
        max_s = 0
        while i < len(nums):
            cur_s = nums[i]
            while i+1< len(nums) and nums[i]<nums[i+1]:
                i+=1
                cur_s+=nums[i]
            max_s = max(max_s,cur_s)
            i+=1
        return max_s
