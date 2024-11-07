class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        first,last = -1,-1
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]<target:
                left = mid+1
            else:
                right = mid-1
        if left < len(nums) and nums[left]==target:
            first = left
        left = 0
        right = len(nums)-1
        while left <=right:
            mid = left+(right-left)//2
            if nums[mid]<=target:
                left = mid+1
            else:
                right = mid-1
        if right >= 0 and nums[right] == target:
            last = right
        return [first,last]   