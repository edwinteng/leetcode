class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def dfs(index,path):
            #if index == len(nums):
            ans.append(path)
                #return
            for i in range(index,len(nums)):
                if i!=index and nums[i-1]==nums[i]:
                    continue
                #dfs(i+1,path)
                dfs(i+1,path+[nums[i]])

        dfs(0,[])
        return ans