class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        
        while i < j:
            mid = i +(j-i)//2
            #if (mid == 0 and nums[mid]!=nums[mid+1]) or (mid==len(nums)-1 and nums[mid]!=nums[mid-1]) or (0<mid<len(nums)-1 and nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]):
            #    return nums[mid]
            #mid = mid+1 and mid %2 = 0 -> right
            if (nums[mid] == nums[mid+1] and mid%2 == 0) or (mid%2==1 and nums[mid] == nums[mid-1]):
                i = mid+1
            else:
                j = mid
        
        return nums[i]