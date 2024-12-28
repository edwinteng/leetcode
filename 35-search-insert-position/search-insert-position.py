class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i, j = 0,len(nums)-1
        while i<=j:
            mid = i+(j-i)//2
            if nums[mid]==target:
                return mid 
            if nums[mid]<target:
                i=mid+1
            else:
                j = mid-1 
        return i