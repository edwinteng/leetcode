class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i,j = 0, len(nums)-1
        ans = []
        while i <=j:
            if abs(nums[i])<abs(nums[j]):
                ans=[nums[j]*nums[j]]+ans
                j-=1
            else:
                ans=[nums[i]*nums[i]]+ans
                i+=1
        return ans