class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        ans = []
        def dfs(index,path):
            ans.append(path)
            for i in range(index,len(nums)):
                if i==index or nums[i]!=nums[i-1]:
                    dfs(i+1,path+[nums[i]])
        dfs(0,[])
        return ans