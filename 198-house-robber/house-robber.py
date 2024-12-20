class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)

        prev_prev,prev = nums[0],max(nums[1],nums[0])
        for num in nums[2:]:
            
            cur = max(num+prev_prev,prev)
            prev_prev = prev
            prev = cur
        return cur

