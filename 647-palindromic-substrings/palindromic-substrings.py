class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans =0
        for i in range(len(s)):
            #odd
            width=0
            while i-width>=0 and i+width<len(s) and s[i-width]==s[i+width]:
                ans+=1
                width+=1
            #even
            width=0
            while i-width>=0 and i+1+width<len(s) and s[i-width]==s[i+width+1]:
                ans+=1
                width+=1
        return ans
