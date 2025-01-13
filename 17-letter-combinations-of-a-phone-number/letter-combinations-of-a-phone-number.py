class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans = []
        def dfs(index,path):

            if index == len(digits):
                ans.append(path)
                return
            for c in d[digits[index]]:
                dfs(index+1,path+c)
        dfs(0,'')
        return ans if len(digits)>0 else []
