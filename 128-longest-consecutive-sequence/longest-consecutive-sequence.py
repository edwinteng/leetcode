class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use a set to keep track of the occurrence of numbers
        # go through the list and go through the list
        # keep track of the length of sequence
        d = set(nums)
        ans = 0
        for num in nums:
            if num-1 not in d:
                num_check = num
                while num_check in d:
                    num_check+=1
                ans = max(ans,num_check-num)
        return ans