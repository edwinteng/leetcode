class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_length = len(strs[0])
        prefix = ''
        for i in range(max_length):
            char = strs[0][i]
            for j in range(1,len(strs)):
                if i == len(strs[j]) or char != strs[j][i]:
                    return prefix
            prefix=prefix+char 
        return prefix