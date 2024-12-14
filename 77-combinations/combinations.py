class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def dfs(count,start,path):
            if count==k:
                ans.append(path)
                return
            for i in range(start,n+1):
                dfs(count+1,i+1,path+[i])
        dfs(0,1,[])
        return ans