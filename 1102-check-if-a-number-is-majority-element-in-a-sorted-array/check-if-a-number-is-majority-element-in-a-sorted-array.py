class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        for i in range(len(nums)):
            if target == nums[i] and i+len(nums)//2< len(nums) and nums[i]==nums[i+len(nums)//2]:
                return True
        return False