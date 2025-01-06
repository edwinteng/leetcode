class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d_t = [0]*26
        for i in range(len(s1)):
            d_t[ord(s1[i])-ord('a')]+=1
        d_w = [0]*26
        valid = 0
        for right,c in enumerate(s2):
            d_w[ord(c)-ord('a')]+=1
            left = right-len(s1)
            if left>=0:
                d_w[ord(s2[left])-ord('a')]-=1
            left+=1
            if d_t==d_w:
                return True
        return False
