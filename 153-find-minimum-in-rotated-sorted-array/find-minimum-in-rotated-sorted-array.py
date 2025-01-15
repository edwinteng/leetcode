class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        ans = float('Inf')
        while left<=right:
            mid = left+ (right-left)//2
            if nums[mid]<nums[right]:
                right = mid-1
                ans = min(ans,nums[mid])
            else:
                left = mid+1
                ans = min(ans,nums[right])
        return ans