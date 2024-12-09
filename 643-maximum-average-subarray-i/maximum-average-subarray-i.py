class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k >=len(nums):
            return sum(nums)/len(nums)
        
        win_sum = sum(nums[:k])
        max_sum = win_sum
        for right in range(k,len(nums)):
            win_sum=win_sum+nums[right]-nums[right-k]
            max_sum = max(win_sum,max_sum)
        return max_sum/k