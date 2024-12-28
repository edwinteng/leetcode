class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def dfs(left,right,path):
            if left ==n and right==n:
                ans.append(path)
                return
            
            if left < n:
                dfs(left+1,right,path+'(')
            if right<left:
                dfs(left,right+1,path+')')
        dfs(0,0,'')
        return ans
