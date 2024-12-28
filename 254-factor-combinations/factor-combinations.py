class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(val,start,path):
            if len(path)>0:
                ans.append(path+[val])
                
            
            for n in range(start,int(sqrt(val))+1):
                if val%n == 0:
                    dfs(val//n,n,path+[n])
        dfs(n,2,[])
        return ans



   
