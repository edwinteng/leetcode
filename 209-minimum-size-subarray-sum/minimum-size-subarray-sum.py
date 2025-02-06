class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        left = 0
        min_size = len(nums)+1
        for right in range(len(nums)):
            total+=nums[right]
            while  total>=target:
                min_size = min(min_size,right-left+1)
                total-=nums[left]
                left+=1

        return min_size if min_size<=len(nums) else 0