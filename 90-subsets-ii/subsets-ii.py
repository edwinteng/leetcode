class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def dfs(cur,path):
            if cur==len(nums):
                ans.append(path)
                return 
            ans.append(path)
            for i in range(cur,len(nums)):
                if cur==i or nums[i]!=nums[i-1]:
                    dfs(i+1,path+[nums[i]])
        dfs(0,[])
        return ans