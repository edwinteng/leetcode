class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def dfs(index,total,path):
            if total>n:
                return 
            if len(path)>k or (len(path)==k and total!=n):
                return 
            if total==n and len(path)==k:
                ans.append(path)
                return 
            for i in range(index,10):
                if total+i <=n:
                    dfs(i+1,total+i,path+[i])
        dfs(1,0,[])
        return ans