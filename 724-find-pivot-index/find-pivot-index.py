class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        prefix_sum = [0]*len(nums)
        if len(nums) and total_sum-nums[0]==0:
            return 0
        for i in range(1,len(nums)):
            prefix_sum[i] = prefix_sum[i-1]+nums[i-1]
            if prefix_sum[i]*2 == (total_sum-nums[i]):
                return i
        return -1        