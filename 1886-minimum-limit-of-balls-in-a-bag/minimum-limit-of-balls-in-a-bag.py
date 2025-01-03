class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        i,j =  1,max(nums)
        def helper(limit):
            count = 0
            for num in nums:
                #temp = num
                #while temp >limit:
                #    temp-=limit
                count+=(ceil(num/limit)-1)
            return count
        
        while i < j:
            mid = i+((j-i)//2)
            
            if helper(mid)>maxOperations: # # of operation<maxOperation increase limit 
                i=mid+1
            else:
                j = mid
        return i
