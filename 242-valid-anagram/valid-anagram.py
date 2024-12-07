class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s): return False
        d_t = [0]*26
        d_s = [0]*26
        for char in s:
            d_s[ord(char)-ord('a')]+=1
        for char in t:
            d_t[ord(char)-ord('a')]+=1
        return d_s==d_t