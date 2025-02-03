class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing,decreasing = 1,1
        ans = 1
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                decreasing+=1
            else:
                decreasing = 1
            if nums[i]<nums[i+1]:
                increasing+=1
            else:
                increasing=1
            ans = max(ans,increasing,decreasing)
        return ans
