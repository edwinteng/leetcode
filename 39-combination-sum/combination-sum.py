class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(path,index,total):
            if total == target:
                ans.append(path)
                return 
            if total> target:
                return
            for i in range(index,len(candidates)):
                dfs(path+[candidates[i]],i,total+candidates[i])

        dfs([],0,0)
        return ans

