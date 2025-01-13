class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        ans = []
        def dfs(num,prev,path):
            if len(path)>0:
                ans.append(path+[num])
            for i in range(prev,int(sqrt(num))+1):
                if num%i == 0:
                    dfs(num/i,i,path+[i])
        dfs(n,2,[])
        return ans if n>1 else []