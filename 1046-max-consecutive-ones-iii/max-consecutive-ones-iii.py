class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,tmp_k = 0, k
        ans = 0
        for right in range(len(nums)):
            if nums[right]==0:
                tmp_k-=1
            while tmp_k < 0 and left <= right:
                if nums[left]==0:       
                    tmp_k+=1
                left+=1
            ans = max(ans,right-left+1)
        return ans