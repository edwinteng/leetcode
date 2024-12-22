class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        ans = []
        def dfs(index,path):
            if index == len(s):
                ans.append(' '.join(path))
                return
            #loop through dict and check if s startwith any word
            for word in wordDict:
                if s[index:].startswith(word):
                    dfs(index+len(word),path+[word])
        dfs(0,[])
        return ans
        