class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(index,total,path):
            if total==target:
                ans.append(path)
            if index<len(candidates) and total<target:
                dfs(index,total+candidates[index],path+[candidates[index]])
                dfs(index+1,total,path)
        dfs(0,0,[])
        return ans
