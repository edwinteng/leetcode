class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        left = 0
        min_length = len(nums)+1
        for right,num in enumerate(nums):
            total+=num
            while left <= right and total>=target :
                min_length = min(min_length,right-left+1)
                total-=nums[left]
                left+=1
                
        return min_length if min_length<=len(nums) else 0