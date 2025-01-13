class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def dfs(index,path):
            if index == len(s):
                ans.append(path)
                return
            #for i in range(index,len(s)):
            if s[index].isalpha():
                dfs(index+1,path+s[index].upper())
                dfs(index+1,path+s[index].lower())
            #upper case 
            #lower case
            else:
                dfs(index+1,path+s[index])
        dfs(0,'')
        return ans