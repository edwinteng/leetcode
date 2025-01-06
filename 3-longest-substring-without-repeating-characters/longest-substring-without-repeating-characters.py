class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        ans = 0
        left = 0
        for right,c in enumerate(s):
            d[c]=d.get(c,0)+1
            # while repeat 
            while left < right and d[c]>1:
                d[s[left]]-=1
            # remove
                left+=1
            ans=max(ans,right-left+1)
            # update length
        return ans