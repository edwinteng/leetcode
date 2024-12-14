class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def dfs(index,path):
            #if index == len(nums):
            ans.append(path)
                #return
            for i in range(index,len(nums)):
                if i==index or (i-1>=0 and nums[i-1]!=nums[i]):
                    dfs(i+1,path+[nums[i]])

        dfs(0,[])
        return ans