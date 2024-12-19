from random import randint
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def quicksort(left,right):
            if left >= right:
                return
            pivot = nums[randint(left,right)]
            less_ptr,right_ptr,current=left-1,right+1,left
            while current < right_ptr:
                if nums[current]<pivot:
                    less_ptr+=1
                    nums[current],nums[less_ptr]=nums[less_ptr],nums[current]
                    current+=1
                elif nums[current]>pivot:
                    right_ptr-=1
                    nums[current],nums[right_ptr]=nums[right_ptr],nums[current]
                    #current+=1
                else:
                    current+=1
            quicksort(left,less_ptr)
            quicksort(right_ptr,right)
        quicksort(0,len(nums)-1)
        return nums



