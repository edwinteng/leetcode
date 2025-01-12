class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(left,right,path):
            if left==n and left==right:
                ans.append(path)
                return
            if left < n:
                dfs(left+1,right,path+'(')
            if right < left:
                dfs(left,right+1,path+')')
        dfs(0,0,'')
        return ans
