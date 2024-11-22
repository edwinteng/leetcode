class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize product
        product = [1]*len(nums)
        # calculate prefix
        for i in range(1,len(nums)):
            product[i]=product[i-1]*nums[i-1]
        
        postfix = 1
        # loop from the end to the beginning
        for i in range(len(nums)-1,-1,-1):
        # calculate product 
            product[i] = product[i]*postfix
            postfix = postfix*nums[i]
        # return product
        return product