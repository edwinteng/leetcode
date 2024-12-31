class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        mask = [False]*len(nums)
        ans = []
        def dfs(index,path):
            if index == len(nums):
                ans.append(path)
                return

            for i in range(len(nums)):
                if mask[i] == False:
                    mask[i] = True
                    dfs(index+1,path+[nums[i]])
                    mask[i] = False
        dfs(0,[])
        return ans