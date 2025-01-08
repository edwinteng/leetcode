class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if len(nums)==0:
            return [[lower,upper]]
        ans = []
        nums=[lower-1]+nums
        nums = nums+[upper+1]
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>1:
                ans.append([nums[i-1]+1,nums[i]-1])
        return ans

