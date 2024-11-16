class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1= [0]*256
        d2 = [0]*256
        i = 1
        for c1,c2 in zip(s,t):
            if d1[ord(c1)] != d2[ord(c2)]:
                return False
            d1[ord(c1)],d2[ord(c2)] = i,i
            i+=1
        return True