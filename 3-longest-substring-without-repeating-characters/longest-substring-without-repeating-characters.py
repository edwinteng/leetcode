class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        ans = 0
        left = 0
        for right,c in enumerate(s):
            while left < right and c in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[right])
            ans=max(ans,right-left+1)
        return ans