class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #write_ptr, write pointer,  0<=write_ptr<len(nums)
        #input: nums
        if len(nums) == 0:
            return 0
        write_ptr = 0
        freq = 1
        #return length of ans
        for num in nums[1:]:
            if num == nums[write_ptr]: # num == nums[write_ptr]
                if freq == 1: #    if freq ==1:
                    write_ptr+=1   
                    nums[write_ptr] = num  #        write
                    freq+=1
            else: 
                # num != nums[write_ptr]
                write_ptr +=1 #    move write_ptr+1
                nums[write_ptr] = num #    write 
                freq = 1 #    freq = 1
                # frequency of num
        return write_ptr+1
