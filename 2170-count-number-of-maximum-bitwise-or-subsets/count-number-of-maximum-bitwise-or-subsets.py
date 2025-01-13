class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = 0
        max_or = 0
        for num in nums:
            max_or |= num
        
        def dfs(index,bitsum):
            nonlocal ans
            if bitsum==max_or:
                ans=ans+1
            for i in range(index,len(nums)):
                dfs(i+1,bitsum|nums[i])
        dfs(0,0)
        return ans
