class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = [0]*26
        d2 = [0]*26
        for c in s:
            d[ord(c)-ord('a')]+=1
        for c in t:
            d2[ord(c)-ord('a')]+=1
        return d==d2