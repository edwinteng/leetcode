class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #brute force
        # take max of nums
        # loop thrugh the list 
        # do a loop through min to max
        # get the length of max
        #
        # use a set to keep track of the occurrence of numbers
        # go through the list and go through the list
        # keep track of the length of sequence
        mem = set(nums)
        max_len = 0
        
        for num in nums:
            if num-1 not in mem:
                cur_num = num
                while cur_num in mem:
                    cur_num+=1
                max_len = max(max_len,cur_num-num)
        return max_len