class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(index,path):
            if index == len(nums):
                #print('add '+str(index))
                ans.append(path)
                return
            #print(str(index)+':'+str(len(nums)))

            dfs(index+1,path+[nums[index]])
            dfs(index+1,path)
        dfs(0,[])
        return ans
