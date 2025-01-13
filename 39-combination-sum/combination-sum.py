class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(index,path,total):
            if total > target:
                return
            if total==target:
                ans.append(path)
                return
            for i in range(index,len(candidates)):
                dfs(i,path+[candidates[i]],total+candidates[i])
        dfs(0,[],0)
        return ans

