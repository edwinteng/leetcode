class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def dfs(index,total,path):
            if total==target:
                ans.append(path)
                return
            if index == len(candidates) or total>target:
                return
            for i in range(index,len(candidates)):
                if index!=i and candidates[i]==candidates[i-1]:
                    continue
                dfs(i+1,total+candidates[i],path+[candidates[i]])
        dfs(0,0,[])
        return ans
