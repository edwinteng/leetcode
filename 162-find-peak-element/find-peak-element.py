class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-2
        while left<= right:
            mid = left+(right-left)//2
            if nums[mid]>nums[mid+1]:
                right = mid-1
            else:
                left = mid+1
        return left