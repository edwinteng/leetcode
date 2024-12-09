class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(path,index,total):
            if total==target:
                ans.append(path)
            #if total >target or index >= len(candidates):
            #    return
            #total < target  or  index != len(candidates)
            #add self
            #print(path)
            #print(index)
            if total < target and index <len(candidates):
                dfs(path,index+1,total)
                dfs(path+[candidates[index]],index,total+candidates[index])
            #not add self
        
            
        dfs([],0,0)
        return ans

