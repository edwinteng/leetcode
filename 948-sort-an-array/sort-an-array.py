from random import randint
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        pivot = nums[randint(0,len(nums)-1)]
        left = [n for n in nums if n < pivot]
        equal = [n for n in nums if n==pivot]
        right = [n for n in nums if n>pivot]
        return self.sortArray(left)+equal+self.sortArray(right)