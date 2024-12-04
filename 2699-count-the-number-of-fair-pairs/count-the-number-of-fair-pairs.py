from bisect import bisect_left
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def bin_search(left,right,target):
            while left <=right:
                mid = left+(right-left)//2
                if nums[mid]<target:
                    left = mid+1
                else:
                    right = mid-1
            return right
        nums.sort()
        
        num_pair = 0
        for i,x in enumerate(nums):
            #left_index = bisect_left(nums,lower-x,i+1)
            #right_index = bisect_left(nums,upper-x+1,i+1)
            left_index = bin_search(i+1,len(nums)-1,lower-x)
            right_index = bin_search(i+1,len(nums)-1,upper-x+1)
            num_pair += (right_index-left_index)
        return num_pair